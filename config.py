
# "{http://pdm_revisao_2020out_dp}po1a_cqs_qsfuncional_pl"

CONFIG_CAMPOS = {

	# Cart Qual Solo
	"{http://pdm_revisao_2020out_dp}po1a_cqs_.*": {
		"cod_dmpu": ["Código DMPU", None],
		"dominio_dm": ["Domínio", None],
		"tema_dmpu": ["Tema", None],
		"tipo": ["Tipo", None],
		"designa": ["Designação", None],
		"designacao": ["Designação", None],
		"numero": ["Número", None],
		"descricao": ["Descrição", None],
		"class": ["Classificação", None],
		"t_espaco": ["Categoria de espaço", "QS_TE_QSF"],
		"st_espaco": ["Sub categoria de espaço", "QS_TEQSF_2"],
		"shape_area": ["",None],
		"shape_length": ["",None],
		"boundedBy": ["", None]
	},
	"{http://pdm_revisao_2020out_dp}po1a_cqs_crodoviarios_ln": {
		"tipologia": [ "Tipologia", None ],
		"tip_rede_m": [ "Tipologia da rede de serviço municipal", None ],
		"situacao": ["Situação", "SITUACAO"],
		"tip_estrut": ["Tipo de estrutura", "PV_T_ESTRUTURA"]
	},
	
	# Cart Cond
	"{http://pdm_revisao_2020out_dp}pc1_ccg_.*": {
		"cod_dmpu": ["Código DMPU", None],
		"dominio_dm": ["Domínio", None],
		"tema_dmpu": ["Tema", None],
		"classifica": ["Classificação", None],
		"diploma_p": ["Diploma", None],
		"shape_area": ["",None],
		"boundedBy": ["", None],
		"designa": ["Designação", None],
		"descricao": ["Descrição", None],
		"t_protecao": ["Tipo de proteção", None],
		"diploma_pr": ["Diploma proteção", None],
		"legislac_1": ["Legislação", None]
	},
	"{http://pdm_revisao_2020out_dp}pc1_ccg_civpatrimonial_pl": {
		"proteção": ["Proteção", None],
		"designaç": ["Designação", None],
		"topónimo": ["Topónimo", None],
		"tipificaç": ["Tipificação", None],
		"propriedad": ["Propriedade", None],
		"estado_de_": ["Estado conservação",None],
		"tipo_de_pr": ["Tipo de proteção", None],
		"tipo_de_cl": ["Tipo de classificação", None],
		"descriçã": ["Descrição", None],
		"observaç": ["Observações", None],
		"categoriza": ["Categorização", None]
	},
	"{http://pdm_revisao_2020out_dp}pc1_ccg_sobreiros_pl": {
		"local": ["Local", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_aapublico_pl": {
		"processo": ["Processo", None],
		"especie": ["Especie", None],
		"nom_vulgar": ["Nome vulgar", None],
		"quant": ["Quantidade", None, "{:d}"],
		"raio_prot": ["Raio proteção", None, "{:.1f} m"],		
		"tipo": ["Tipificação", "SP_AIP_TIPO"],
		"situacao": ["Situação atual", "SP_CLASS"],
		"local": ["Local", None],
		"obs": ["Observações", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_zsaagua_pl": {
		"obs": ["Observações", None],
		"legislac_1": ["Legislação", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_zsreletrica_pl": {
		"local": ["Localização", None],
		"tipologia": ["Tipologia", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_dnacional_pl": {
		"tipo": ["Tipo", None],
		"local": ["Local", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_rrnedesclassificadas_pl": {
		"tipo": ["Tipo", None],
		"tipo1": ["Tipologia", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_ideeletrica_ln": {
		"local": ["Localização", None],
		"tipologia": ["Tipologia", None],
		"situacao": ["Situação", None],
		"shape_leng": ["",None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_iteeletrica_ln": {
		"local": ["Localização", None],
		"tipologia": ["Tipologia", None],
		"shape_leng": ["",None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_fpesada_ln": {
		"designac_2": ["Designação", None],
		"tipologia": ["Tipologia", None],
		"shape_leng": ["",None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_itreletrica_pt": {
		"transf_ten": ["Tensões", None],
		"tipologia": ["Tipologia", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_aaipublico_pt": {
		"processo": ["Processo", None],
		"especie": ["Especie", None],
		"nom_vulgar": ["Nome vulgar", None],
		"quant": ["Quantidade", None, "{:d}"],
		"raio_prot": ["Raio proteção", None, "{:.1f} m"],		
		"tipo": ["Tipificação", "SP_AIP_TIPO"],
		"situacao": ["Situação atual", "SP_CLASS"],
		"local": ["Local", None],
		"obs": ["Observações", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_mgeodesicos_pt": {
		"local": ["Localização", None],
		"descricao": ["Descrição", None],
		"tipo_coord": ["Tipo coordenadas", None],
		"m": ["M", None],
		"p": ["P", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_fosmaritimo_pt": {
		"tipo": ["Tipo", None],
		"obs": ["Observações", None]
	},	
	"{http://pdm_revisao_2020out_dp}pc1_ccg_civpatrimonial_pt": {
		"localizaca": ["Localização", None],
		"designac_2": ["Designação", None],
		"tipo_class": ["Tipo classificação", None]
	},	
	
	# Estr Ecologica
	"{http://pdm_revisao_2020out_dp}po1b_ceem_.*": {
		"cod_dmpu": ["Código DMPU", None],		
		"dominio_dm": ["Domínio", None],
		"tema_dmpu": ["Tema", None],
		"classifica": ["Classificação", None],
		"diploma_p": ["Diploma", None],
		"shape_area": ["",None],
		"boundedBy": ["", None],
		"designa": ["Designação", None],
		"designac_2": ["Designação", None],
		"designaç": ["Designação", None],
		"tipo": ["Tipo", None],
		"tipologia": ["Tipologia", None],
		"toponimo": ["Toponimo", None],
		"subcategor": ["Subcategoria", None],
		"situação": ["Situação", None],
		"situacao": ["Situação", None],
		"descricao": ["Descrição", None]
	},
	"{http://pdm_revisao_2020out_dp}po1b_ceem_avevecologico_pl": {
		"acess_livr": ["Acesso", None]
	},
	"{http://pdm_revisao_2020out_dp}po1b_ceem_avapublico_pl": {
		"v_patrimon": ["Valor patrimonial", None],
		"t_acesso": ["Tipo acesso", None],
		"rep_qsolo": ["Representação Q.Solo", None],
		"rep_uopg": ["Representação UOPG", None],
		"ação_progr": ["Ação programa", None]
	},
	"{http://pdm_revisao_2020out_dp}po1b_ceem_rconexao_pl": {
		"texto": ["Texto", None]
	},
	"{http://pdm_revisao_2020out_dp}po1b_ceem_lagua_ln": {
		"identidade": ["Identidade", None],
		"arruamento": ["Arruamento", None],
		"tipoassent": ["Tipo de assentamento", None],		
		"bacia": ["Bacia", None],
		"shape_leng": ["",None]
	},	
	"{http://pdm_revisao_2020out_dp}po1b_ceem_srhomogeneas_pl": {
		"prof": ["PROF", None],
		"srh": ["SRH", None],
		"f3funcoes": ["3 funções", None]		
	},	
	"{http://pdm_revisao_2020out_dp}po1b_ceem_cecologico_pl": {
		"prof": ["PROF", None],
		"srh": ["SRH", None],
		"f3funcoes": ["3 funções", None]		
	},	
	
	# Riscos Naturais
	"{http://pdm_revisao_2020out_dp}po1c_crn_.*": {
		"cod_dmpu": ["Código DMPU", None],		
		"dominio_dm": ["Domínio", None],
		"tema_dmpu": ["Tema", None],
		"classifica": ["Classificação", None],
		"diploma_p": ["Diploma", None],
		"shape_area": ["",None],
		"boundedBy": ["", None],
		"designa": ["Designação", None],
		"designac_2": ["Designação", None],
		"designaç": ["Designação", None],
		"tipo": ["Tipo", None],
		"tipologia": ["Tipologia", None],
		"toponimo": ["Toponimo", None],
		"subcategor": ["Subcategoria", None],
		"situação": ["Situação", None],
		"situacao": ["Situação", None],
		"descricao": ["Descrição", None]
	},
	"{http://pdm_revisao_2020out_dp}po1c_crn_ainundaveis_pl": {
		"obs": ["Observações", None]		
	},	
	"{http://pdm_revisao_2020out_dp}po1c_crn_lagua_ln": {
		"identidade": ["Identidade", None],
		"arruamento": ["Arruamento", None],
		"tipoassent": ["Tipo de assentamento", None],		
		"bacia": ["Bacia", None],
		"shape_leng": ["",None]
	},	
	
	# Zonamento acústico
	"{http://pdm_revisao_2020out_dp}po1d_cza_zacustico_pl": {
		"cod_dmpu": ["Código DMPU", None],		
		"dominio_dm": ["Domínio", None],		
		"tema_dmpu": ["Tema", None],
		"designac_2": ["Designação", None],
		"tipo_esp_v": ["Tipologia espaços verdes", None],
		"tipo_za": ["Tipo zonamento acústico", None],		
		"shape_area": ["",None],
		"boundedBy": ["", None]
	},	
	
	# Património I
	"{http://pdm_revisao_2020out_dp}po1e_cp1_.*": {
		"cod_dmpu": ["Código DMPU", None],		
		"dominio_dm": ["Domínio", None],		
		"tema_dmpu": ["Tema", None],
		"designaç": ["Designação", None],
		"observaç": ["Observações", None],
		"caracteriz": ["Caracterização", None],
		"data_da_in": ["Data de Vigência - Inicio", None],
		"lista": ["Lista", None],
		"classifica": ["Classificação", None],
		"diploma_p": ["Diploma", None],
		"shape_area": ["",None],
		"boundedBy": ["", None],
		"designa": ["Designação", None],
		"designac_2": ["Designação", None],
		"tipo": ["Tipo", None],
		"tipologia": ["Tipologia", None],
		"toponimo": ["Toponimo", None],
		"subcategor": ["Subcategoria", None],
		"situação": ["Situação", None],
		"descricao": ["Descrição", None]
	},		
	"{http://pdm_revisao_2020out_dp}po1e_cp1_aapublico_pl": {
		"processo": ["Processo", None],
		"especie": ["Especie", None],
		"nom_vulgar": ["Nome vulgar", None],
		"quant": ["Quantidade", None, "{:d}"],
		"raio_prot": ["Raio proteção", None, "{:.1f} m"],		
		"tipo": ["Tipificação", "SP_AIP_TIPO"],
		"situacao": ["Situação atual", "SP_CLASS"],
		"local": ["Local", None],
		"legislac_1": ["Legislação", None],
		"obs": ["Observações", None]
	},	
	"{http://pdm_revisao_2020out_dp}po1e_cp1_zpicvclassificacao_pl": {
		"legislac_1": ["Legislação", None],
		"t_protecao": ["Tipo de proteção", None]
	},		
	"{http://pdm_revisao_2020out_dp}po1e_cp1_civpatrimonial_pl": {
		"topónimo": ["Topónimo", None],
		"tipificaç": ["Tipificação", None],
		"estado_de_": ["Estado conservação",None],
		"categoriza": ["Categorização", None],
		"descriçã": ["Descrição", None],
		"tipo_de_pr": ["Tipo de proteção", None],
		"propriedad": ["Propriedade", None]
	},		
	"{http://pdm_revisao_2020out_dp}po1e_cp1_znaedificandi_pl": {
		"n_identifi": ["Núm. de identificação", None],
		"diploma_pr": ["Diploma de proteção", None]
	},		
	"{http://pdm_revisao_2020out_dp}po1e_cp1_aaipublico_pt": {
		"processo": ["Processo", None],
		"especie": ["Especie", None],
		"nom_vulgar": ["Nome vulgar", None],
		"quant": ["Quantidade", None, "{:d}"],
		"raio_prot": ["Raio proteção", None, "{:.1f} m"],		
		"tipo": ["Tipificação", "SP_AIP_TIPO"],
		"situacao": ["Situação atual", "SP_CLASS"],
		"local": ["Local", None],
		"legislac_1": ["Legislação", None],
		"obs": ["Observações", None]
	},	
	"{http://pdm_revisao_2020out_dp}po1e_cp1_civpatrimonial_pt": {
		"tipo_class": ["Tipo classificação", None],
		"localiza": ["Localização", None],
	},	
		
	# Patrimonio II
	"{http://pdm_revisao_2020out_dp}po1f_cp2_asarqueologica_pl": {
		"cod_dmpu": ["Código DMPU", None],		
		"dominio_dm": ["Domínio", None],		
		"tema_dmpu": ["Tema", None],
		"designaç": ["Designação", None],
		"observaç": ["Observações", None],
		"shape_area": ["",None],
		"boundedBy": ["", None],
		"designa": ["Designação", None],
		"designac_2": ["Designação", None],
		"toponimo": ["Toponimo", None],
		"descricao": ["Descrição", None],
		"tipo_de_pe": ["Tipo de perímetro arquelógico", None],
		"tipo_de_ma": ["Tipo de matriz", None]
	},	
	
	# Estr viária  
	"{http://pdm_revisao_2020out_dp}po1g_ceve_.*": {
		"cod_dmpu": ["Código DMPU", None],		
		"dominio_dm": ["Domínio", None],		
		"tema_dmpu": ["Tema", None],
		"designaç": ["Designação", None],
		"observaç": ["Observações", None],
		"caracteriz": ["Caracterização", None],
		"shape_area": ["",None],
		"boundedBy": ["", None],
		"designa": ["Designação", None],
		"designac_2": ["Designação", None],
		"tipo": ["Tipo", None],
		"tipologia": ["Tipologia", None],
		"toponimo": ["Toponimo", None],
		"tip_rede_m": [ "Tipologia da rede de serviço municipal", None ],
		"situacao": ["Situação", "SITUACAO"],
		"tip_estrut": ["Tipo de estrutura", "PV_T_ESTRUTURA"],
		"descricao": ["Descrição", None]
	},		
	
	
	# Elementos adicionais Comp.Urb e SRU
	"{http://pdm_revisao_2020out_dp}oea3e_agurbanistica_2": {
		"nud_capa": ["NUP", None],
		"desc_tipo_": ["tipo", None],
		"requerente": ["Requerente", None],
		"toponimo": ["Topónimo", None],
		"desc_oper_": ["Tipo de operação urbanística", None],
		"aprov_arq_": ["Aprovação arquitectura", None],
		"obs_regist": ["Observações", None],
		"tipologia": ["Tipologia", None],
		"aprov_ar_1": ["Data aprov. arquitectura", None],
		"shape_area": ["",None],
		"boundedBy": ["", None]
	},
	"{http://pdm_revisao_2020out_dp}oea3e_aleurbanisticas": {
		"ano_al": ["Ano do título", None],
		"num_titulo": ["Número do título", None],
		"tip_espurb": ["Tipo de especificação", None],
		"design": ["Designação", None],
		"toponimo": ["Topónimo", None],
		"data_despa": ["Data despacho", None],
		"aprov_arq1": ["Data aprov. arquitectura", None],
		"shape_area": ["",None],
		"boundedBy": ["", None]
	},
	"{http://pdm_revisao_2020out_dp}oea3e_ocurbanisticos": {
		"toponimo": ["Topónimo", None],
		"tipologia": ["Tipologia", "CU_T_OCU"],
		"t_gpatr": ["Tipologia gestão patrimonial", "CU_TGPATR"],
		"nup": ["NUP", None],
		"titular": ["Titular", None],
		"id_parcela": ["Parcela", None],
		"pjudicial": ["Processo judicial", None],
		"tip_ot": ["Tipologia outros títulos", None],
		"n_processo": ["Número do processo", None],
		"tipo_proce": ["Tipo do processo", None],
		"requerente": ["Requerente", None],
		"op_urbanis": ["Tipo de operação urbanística", None],
		"uso": ["Tipo de uso", None],
		"alvará": ["Título", None],
		"data_alvar": ["Data emissão título", None],
		"local_": ["Local", None],
		"shape_area": ["",None],
		"boundedBy": ["", None]
	},
	"{http://pdm_revisao_2020out_dp}oea3e_alv_obras_sru": {
		"n_processo": ["Número do processo", None],
		"tipo_proce": ["Tipo do processo", None],
		"requerente": ["Requerente", None],
		"op_urbanis": ["Tipo de operação urbanística", None],
		"uso": ["Tipo de uso", None],
		"alvara": ["Título", None],
		"data_alvar": ["Data emissão título", None],
		"local_": ["Local", None],
		"boundedBy": ["", None]
	}


	
}

CONFIG_OMIT_AREA = {
	"{http://pdm_revisao_2020out_dp}oea3e_ocurbanisticos": {
		"tipologia": ["OTITUL"]
	}
}

CONFIG_DOMINIOS = {
	"QS_TE_QSF": {
		"TEEC": "Espaços centrais",
		"TEEAE": "Espaços de atividades económicas",
		"TEEVFAR": "Espaços verdes e Frente atlântica e ribeirinha",
		"TEEUEE": "Espaços de uso especial - Equipamentos",
		"TEEUEI": "Espaços de uso especial - Infraestruturas",
		"TEEUBD": "Espaços urbanos de baixa densidade"
	},
	"QS_TEQSF_2": {
		"TE2AH": "Área histórica",
		"TE2AFUCT1": "Área de frente urbana contínua de tipo I",
		"TE2AFUCT2": "Área de frente urbana contínua de tipo II",
		"TE2ABIIL": "Área de blocos isolados de implantação livre",
		"TE2AAET1": "Área de atividades económicas de tipo I",
		"TE2AAET2": "Área de atividades económicas de tipo II",
		"TE2AFAR": "Área de frente atlântica e ribeirinha",
		"TE2AVFC": "Área verde de fruição coletiva",
		"TE2AVLP": "Área verde lúdico-produtiva",
		"TE2AVAE": "Área verde associada a equipamento",
		"TE2AVPE": "Área verde de proteção e enquadramento",
		"TE2AI": "Área de infraestruturas",
		"TE2EUBD": "Espaços urbanos de baixa densidade",
		"TE2AETM": "Área de edifícios de tipo moradia",
		"TE2AE": "Área de equipamentos"
	},
	"CU_TGPATR": {
		"EXPR": "Expropriações",
		"PERM": "Permutas",
		"CED": "Cedências",
		"HP": "Hastas Públicas"	
	},
	"CU_T_OCU": {
		"PGPATR": "Processos de gestão patrimonial",
		"PPTER": "Processos de planeamento territorial",
		"OTITUL": "Outros Títulos"
	},
	"SP_AIP_TIPO": {
		"EI": "Exemplar isolado",
		"CA": "Conjunto arvóreo",
		"A": "Alameda",
		"A_AL": "Alameda (alinhamento)"
	},
	"SP_CLASS": {
		"CL": "Classificado",
		"VC": "Em vias de classificação"
	},
	"PV_T_ESTRUTURA": {
		"CORR": "Corrente",
		"PONT": "Ponte",
		"TUN": "Túnel",
		"VIAD": "Viaduto"
	},
	"SITUACAO": {
		"E": "Existente",
		"P": "Proposta"	
	},

}

KEEP_ID = False

# ########################################################################


URLBASE = {
	"interno": "http://guia-geovista.cm-porto.net/geoserver",
	"externo": "http://marselha.cm-porto.net/innergeosrvr"
}

FEATINFO_MODE = "xml"

 # Para testes

THE_REQ_old = """http://marselha.cm-porto.net/innergeovista/geoserver/PDM_revisao_2020out_DP/ows?service=WMS&version=1.3.0&sld_version=1.1.0&request=GetFeatureInfo&crs=EPSG%3A4326&bbox=41.112397138343539,-8.6757007047338028,41.20397757365015,-8.5627343001683887&format=image%2Fpng&width=721&height=774&layers=PDM_revisao_2020out_DP%3Apo1a_cqs_qsfuncional_pl&styles=&info_format=text/xml", "%20subtype=gml/3.1.1&I=359&J=358&query_layers=PDM_revisao_2020out_DP%3Apo1a_cqs_qsfuncional_pl"""

THE_REQ = """http://marselha.cm-porto.net/innergeosrvr/PDM_revisao_2020out_DP/wms?SERVICE=WMS&REQUEST=GetMap&FORMAT=image%2Fpng&TRANSPARENT=TRUE&STYLES=PDM_revisao_2020out_DP%3APO1A_CQS_QSFUNCIONAL_PL&VERSION=1.3.0&LAYERS=PDM_revisao_2020out_DP%3Apo1a_cqs_qsfuncional_pl&WIDTH=721&HEIGHT=774&CRS=EPSG%3A3763&BBOX=-43690.28164116145%2C162563.27301693344%2C-37249.70379637573%2C169477.2913967727"""

