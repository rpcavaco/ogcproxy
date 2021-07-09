
import logging

from lxml.html.builder import *
from lxml import etree

def gentable():

	logger = logging.getLogger()

	root = HTML(
		HEAD( TITLE("Hello World") ),
		BODY( CLASS("main"),
			H1("Hello World !")
		)
	)	

	ret = etree.tostring(root, xml_declaration=True, encoding='UTF-8')
	logger.info(f"gentable: {ret}")
	
	return ret # byte string
