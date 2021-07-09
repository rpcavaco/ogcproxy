import requests
import httpx 
import logging
import re


from typing import Optional
from lxml import etree, objectify
from fastapi import FastAPI, Request, Response, HTTPException

from config import CONFIG_CAMPOS, CONFIG_DOMINIOS, CONFIG_OMIT_AREA, URLBASE, FEATINFO_MODE, KEEP_ID
from generate import gentable

DECODE_FORMAT = "latin-1"
REQ_WMS_FIELDS = ["request", "service"]

GML_NAMESPACE = {'g': "http://www.opengis.net/gml"}


def translate_links_xml(p_xml_content):
	logger = logging.getLogger()
	try:
		root = etree.fromstring(p_xml_content)
	except:
		logger.debug(p_xml_content[:80], "...")
		raise

	res = root.xpath("//*[@xlink:href]", namespaces={'xlink': "http://www.w3.org/1999/xlink"})
	for el in res:
		for attr_key in el.keys():
			if attr_key.endswith("href"):
				el.set(attr_key, el.get(attr_key).replace(URLBASE["interno"], URLBASE["externo"]))

	ret = etree.tostring(root, xml_declaration=True, encoding='UTF-8')
	return ret # byte string


def parse_featinfo_xml(p_xml_content):
	# tree = etree.parse("")
	logger = logging.getLogger()
	root = etree.fromstring(p_xml_content)
	fmembers = root.xpath("g:featureMember", namespaces=GML_NAMESPACE)

	if len(fmembers) > 0:

		for featel in fmembers[0]:

			# print("feat class:", featel.tag)
			del featel.attrib["fid"]
			cfg_key = None

			found_keys = []
			for _read_key in CONFIG_CAMPOS.keys():

				if _read_key == featel.tag:
					found_keys.append(_read_key)
				else:
					mr = re.match(_read_key, featel.tag)
					if not mr is None:
						found_keys.append(_read_key)

			if len(found_keys) < 1:
				logger.warn(f"configuracao em falta para a camada '{featel.tag}'")
				miss_fields = []
				for fldel in featel:
					miss_fields.append(fldel.tag[fldel.tag.index('}')+1:])
				logger.info("campos em falta: {}".format(",".join(miss_fields)))

			show_area = True
			area_fld_el = None
			if len(found_keys) > 0:

				cfg_flds = {}
				for fky in found_keys:
					cfg_flds.update(CONFIG_CAMPOS[fky])

				has_cfg_keys = (len(cfg_flds.keys()) > 0)
				for fldel in featel:
					no_ns_name = fldel.tag[fldel.tag.index('}')+1:]
					no_area_values = None
					if fldel.tag in CONFIG_OMIT_AREA.keys():
						if no_ns_name in CONFIG_OMIT_AREA[fldel.tag].keys():
							no_area_values = CONFIG_OMIT_AREA[fldel.tag][no_ns_name]
					if no_ns_name.endswith("id"):
						if KEEP_ID:
							fldel.text = fldel.text.split(".")[-1]
							fldel.tag = "id"
						else:
							featel.remove(fldel)
					elif not no_ns_name in cfg_flds.keys():
						#print("removed:", no_ns_name)
						if has_cfg_keys:
							featel.remove(fldel)
						else:
							if show_area and not no_area_values is None:
								if fldel.text in no_area_values:
									show_area = False
					else:
						fld_name, fld_dom = cfg_flds[no_ns_name][:2]
						if no_ns_name.endswith("area"):
							area_val = float(fldel.text)
							if area_val < 10000:
								area_txt = "{:.1f} m2".format(area_val)
							else:
								area_txt = "{:.4f} ha".format(area_val / 10000.0)
							fldel.text = area_txt.replace(".", ",")
							fldel.tag = "Área"
							area_fld_el = fldel
						elif no_ns_name.endswith("length") or no_ns_name.endswith("leng"):
							len_val = float(fldel.text)
							if len_val < 1000:
								len_txt = "{:.1f} m".format(len_val)
							else:
								len_txt = "{:.4f} km".format(len_val / 1000.0)
							fldel.text = len_txt.replace(".", ",")
							fldel.tag = "Comprimento"
							area_fld_el = fldel
						else:
							if show_area and not no_area_values is None:
								if fldel.text in no_area_values:
									show_area = False
							if len(fld_name) > 0:
								fldel.tag = fld_name.replace(" ", "_")
							had_dom_replacement = False
							if not fld_dom is None:
								if fld_dom in CONFIG_DOMINIOS.keys():
									if fldel.text in CONFIG_DOMINIOS[fld_dom].keys():
										fldel.text = CONFIG_DOMINIOS[fld_dom][fldel.text]
										had_dom_replacement = True
							if not had_dom_replacement:
								if len(cfg_flds[no_ns_name]) >= 3:
									fmt = cfg_flds[no_ns_name][2]
									if "f}" in fmt:
										fldel.text = fmt.format(float(fldel.text))
									elif "d}" in fmt:
										fldel.text = fmt.format(int(float(fldel.text)))
									else:
										fldel.text = fmt.format(fldel.text)

				if not show_area and not area_fld_el is None:
					featel.remove(area_fld_el)

	ret = etree.tostring(root, xml_declaration=True, encoding='UTF-8')
	logger.info(f"parse_featinfo_xml: {ret}")
	
	return ret # byte string

def create_app():

	logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', filename='ogcproxy.log',level=logging.DEBUG)
	logger = logging.getLogger()

	fapp = FastAPI()

	@fapp.get("/{featclass}/wms")
	@fapp.get("/{featclass}/ows")
	async def geosrvrproxy(request: Request):

		qspks = set(request.query_params.keys())
		intrs = qspks.intersection(REQ_WMS_FIELDS)
		missing = set(REQ_WMS_FIELDS).difference(intrs)

		if len(missing) > 0:
			raise HTTPException(status_code=500, detail=f"parametros em falta: {missing}")

		service = request.query_params["service"]
		reqstr = request.query_params["request"]

		if service.lower() != "wms":
			raise HTTPException(status_code=500, detail=f"SERVICE invalido: {service}")

		if "version" in [x.lower() for x in request.query_params.keys()]:
			if "version" in request.query_params.keys():
				version = request.query_params["version"]
			else:
				version = request.query_params["VERSION"]
		else:
			version = "1.0.0"

		use_url = str(request.url).replace(str(request.base_url), "")
		final_url = "/".join((URLBASE["interno"],use_url))

		if reqstr.lower() == "getcapabilities":

			async with httpx.AsyncClient() as client:
				proxy = await client.get(final_url)

			cont = translate_links_xml(proxy.content).decode("utf-8")
			resp = Response(cont, status_code=200, media_type="text/xml")

		elif reqstr.lower() == "getfeatureinfo":
	
			async with httpx.AsyncClient() as client:
				proxy = await client.get(final_url)

			if FEATINFO_MODE.lower() == "html":
				cont = gentable()
				media = "text/html"
			elif FEATINFO_MODE.lower() == "xml":
				cont = parse_featinfo_xml(proxy.content).decode("utf-8")
				media = "text/xml"
			else:
				errstr = f"FEATINFO_MODE invalido: {FEATINFO_MODE.lower()}"
				logger.error(f"FEATINFO_MODE invalido: {FEATINFO_MODE.lower()}")
				raise HTTPException(status_code=500, detail=f"REQUEST invalido: {reqstr}")
			resp = Response(cont, status_code=200, media_type=media)

		elif reqstr.lower() == "getmap":
	
			async with httpx.AsyncClient() as client:
				proxy = await client.get(final_url)
			resp = Response(proxy.content, status_code=200)

		elif reqstr.lower() == "getlegendgraphic":
	
			async with httpx.AsyncClient() as client:
				proxy = await client.get(final_url)
			resp = Response(proxy.content, status_code=200)

		else:
			logger.error(f"REQUEST invalido: {reqstr}")
			raise HTTPException(status_code=500, detail=f"REQUEST invalido: {reqstr}")


		return resp

#	@fapp.get("/{featclass}/ows")
# 	async def owsproxy(request: Request, response: Response, featclass: str, service: Optional[str] = None, layers: Optional[str] = None):

# 		if not service is None and service.lower() != "wms":
# 			raise HTTPException(status_code=500, detail=f"service nao suportado: {service}")

# 		use_url = str(request.url).replace(str(request.base_url), "")
# 		final_url = "/".join((URLBASE["interno"],use_url))

# 		print(request.base_url)
# 		print(request.url)
# 		print("final", final_url)

# 		async with httpx.AsyncClient() as client:
# 			proxy = await client.get(final_url)

# 		resp_content = parse_xml(proxy.content)

# 		response.body = resp_content
# 		response.status_code = proxy.status_code

# 		return response

# 		#cont = teste_xml()
# 		#resp = Response(cont, media_type="text/xml")
			
# #		return resp   

	# Middleware a aplicar a todos os requests
	@fapp.middleware("http")
	async def case_sens_middleware(request: Request, call_next):
		logger = logging.getLogger()
		raw_query_str = request.scope["query_string"].decode(DECODE_FORMAT)

		if len(raw_query_str) > 0:
			new_qs_buffer = []
			splits1 = raw_query_str.split("&")
			for sp1 in splits1:
				splits2 = sp1.split("=")
				try:
					new_qs_buffer.append("{0}={1}".format(splits2[0].lower(), splits2[1]))
				except:
					logger.debug("raw_query_str:{} splits1:{} splits2:{}".format(raw_query_str, splits1, splits2))
					raise	

			new_query_str = "&".join(new_qs_buffer)	
			request.scope["query_string"] = new_query_str.encode(DECODE_FORMAT)

		# path = request.scope["path"].lower()
		# request.scope["path"] = path

		response = await call_next(request)
		return response 

	return fapp	

app = create_app()

# if __name__ == "__main__":
#	teste_xml()


