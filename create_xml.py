#-*- coding: utf-8 -*-
# template code za kreiranje kompleksne xml datoteke


# Elemen in Subelement imata podobna konstruktorja
# Razlika je v parent tagu, ki ga ima Subelement

# Element factory. This function returns an object implementing the Element interface.   
# Element(_tag, attrib=None, nsmap=None, **_extra)

# Subelement factory. This function creates an element instance, and 
# appends it to an existing element.
# SubElement(_parent, _tag, attrib=None, nsmap=None, **_extra)

from lxml import etree


# definiram namespace, ki so v xml-datoteki
ns = {
    'ehr' : "http://www.src.si/schemas/evem/hr/20090909",
    'xsi': "http://www.w3.org/2001/XMLSchema-instance",
}


etree.Element('ImeElementa', 
              nsmap =  dictionary_namespaceov, 
              attrib = dictionary_attributov)

# ce se definira shema
schema_location = 'http://www.src.si/schemas/evem/hr/20090909' # shema za envelope
attrib={'{%s}schemaLocation' % ns['xsi']: schema_location}


# primer, kako je potrebno napisati element, da bo imel spredaj namespace
# pred imenom elementa mora biti namespace v zavitih oklepajih
# '{http://www.src.si/schemas/evem/hr/2009}element'

