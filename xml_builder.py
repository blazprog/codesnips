from lxml import etree

class XmlBuilder(object):
    def __init__(self, root_element, data=None, ns_dict={}):
        self.data = data
        self.root_element_name = root_element
        self.ns_dict = ns_dict
        self.root_element = etree.Element(self.root_element_name, nsmap=ns_dict)
        self.doc = etree.ElementTree(self.root_element)

    def add_sub_element(self, element, parent, element_text='', ns_key=''):
        '''
        helper function for adding subelements, text as parameter
        not calculated
        '''
        if ns_key:
            e = etree.SubElement(parent, '{%s}%s' % (ns[ns_key],element))
        else:
            e = etree.SubElement(parent,element)

        if type(element_text) == float:
            element_text = str(element_text)
        elif type(element_text) == int:
            element_text = str(element_text)
        elif type(element_text) == bool:
            element_text = str(element_text).lower()
        if element_text:
            e.text = element_text
        return e


    def add_element_data(self, element, parent, ns_key=''):
        '''
        helper function for adding subelements, 
        text is read from data helper object
        Hierarchy in helper object is equal than hirarchy in xml document
        '''
        # dodam nov element v xml tree
        if ns_key:
            e = etree.SubElement(parent, '{%s}%s' % (ns[ns_key],element))
        else:
            e = etree.SubElement(parent,element)

        # ko sem dodal element, dodam se tekst elementa,         
        # iscem po hierarhiji objektov, zato rabim vse njegove parente
        parent_name_list = []
        element_parent = e.getparent()

        while element_parent != self.root_element:
            parent_name_list.insert(0, element_parent.tag)
            element_parent = element_parent.getparent()
        print parent_name_list
        element_text = self.data.get_value(parent_name_list, element)
        if type(element_text) == float:
            element_text = str(element_text)
        elif type(element_text) == int:
            element_text = str(element_text)
        elif type(element_text) == bool:
            element_text = str(element_text).lower()
        if element_text:
            e.text = element_text
        return e

    def get_pretty_string(self):
        xml_string = etree.tostring(self.root_element, 
                                    encoding='UTF-8', 
                                    xml_declaration=True, 
                                    pretty_print=True)

        return xml_string

    def write_to_file(self, file_name):
        with open(file_name, 'w') as fobj:
            fobj.write(self.get_pretty_string())


if __name__ == '__main__':
    from catalog import CatalogData
    catalog_data = CatalogData()
    xml_builder = XmlBuilder('catalog', catalog_data)
    book = xml_builder.add_sub_element('book', xml_builder.root_element)
    xml_builder.add_element_data('author', book)
    xml_builder.add_element_data('title', book)
    xml_builder.add_element_data('genre', book)
    xml_builder.add_element_data('publish_date', book)
    xml_builder.add_element_data('description', book)
    print xml_builder.get_pretty_string()
    xml_builder.write_to_file('mybooks.xml')
