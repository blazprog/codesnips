# na osnovi xml fajla kreira kodo,
# ki zgenerira fajl
from __future__ import print_function
from lxml import etree
import re

# XML_FILE = "/home/blaz/Downloads/reki/rekmmmaj.xml"
XML_FILE = "/home/blaz/Desktop/zap_test.xml"
pattern = r"(?P<namespace>\{.*\})?(?P<tag>\w+)"
code_lines = []

def create_code(element, parent=None, indent=0):
    res = re.search(pattern, element.tag)
    namespace = res.group('namespace')
    tag_name = res.group('tag')
    namespaces.add(namespace)
    if parent == None:
        code = "{0} = etree.Element({0}, nsmap=ns)".format(tag_name)
    else:
        res = re.search(pattern, parent.tag)
        if parent == root:
            parent_tag_name = 'root_element'
        else:
            parent_tag_name = res.group('tag')
        # ce ima otroke rabim prireditveni stavek, drugace samo dodam
        if len(element.getchildren()) > 0: 
            code = "{0} = add_element_data({0}, {1})".format(tag_name, parent_tag_name)
        else:
            code = "add_element_data({0}, {1})".format(tag_name, parent_tag_name)
    code_lines.append(code)
    # dodam se kodo za child nodes
    if len(element.getchildren()) > 0:
        for e in element:
            create_code(e, element, indent)

doc = etree.parse(XML_FILE)
root = doc.getroot()
namespaces = set()
create_code(root)

print ('Namespaces in xml document')
for ns in namespaces:
    print (ns)

print('Document generating code')
for line in code_lines:
    print (line)
