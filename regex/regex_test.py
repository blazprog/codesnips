# zamenjava in captured groups

import os
import re
from lxml import etree
old_text = " Formula je yy = xx"
pattern_search = r"\b(?P<lhs>\w+)\b\s+=\s+(?P<rhs>\w+)\b"
pattern_replace = r"\g<rhs> = \g<lhs>"


re = re.compile(pattern_search)


new_text = re.sub(pattern_search, pattern_replace, old_text)
print new_text

# Ali sub deluje s compajliranimi patterni NE!!
# spodnja koda javi napako
# regex_search = re.compile(pattern_search)
# regex_replace = re.compile(pattern_replace)
# new_text = re.sub(regex_search, regex_replace, old_text)
# print new_text



import os
import re
code = """
class MyBraveModel(models.Model)
    _name = 'my_brave_model'
    _description = 'My Brave Model'
    name=fields.char()
    age =          fields.Char()
    born         = fields.Date()
"""    


field_names_pattern = r"(?P<field_name>\w+)\s*=\s*fields[.]"
regex_field_list = re.compile(field_names_pattern)
field_list  = regex_field_list.findall(code)
print field_list

field_names_verbose_pattern = """
    (?P<field_name>\w+)                         #variable name
    \s*                                         #one or more spaces
     =                                          #equal sign 
    \s*                                         #one or more spaces
    fields[.]
"""
regex_field_list = re.compile(field_names_pattern, re.VERBOSE)
field_list  = regex_field_list.findall(code)
print field_list
mo = regex_field_list.match(code)
print mo


model_name_pattern = r"_name\s*=\s*'(?P<model_name>\w+)'"
model_name_regex = re.compile(model_name_pattern)
model_name = model_name_regex.findall(code) # vrne list
print model_name



model_description_pattern = r"_description\s*=\s*'(?P<model_description>.+)'"
model_description_regex = re.compile(model_description_pattern)
match = model_description_regex.search(code)
model_description = match.group('model_description')
print model_description

print 'search example'
match = model_name_regex.search(code)
print 'match.group() => ', match.group()
model_name = match.group('model_name')
print "match.group('model_name') => ", match.group('model_name')
print "match.groups() => ", match.groups()


def add_sub_element(parent,element,element_text='', ns_key=''):
    # helper function for adding subelements
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

def create_odoo_gui(model_name, field_list, model_description=''):
    if not model_description:
        model_description = model_name

    openerp = etree.Element('openerp')
    data = add_sub_element(openerp, 'data')


    # 1. create tree view
    record = add_sub_element(data, 'record')
    record.attrib['model'] = "ir.ui.view"
    record.attrib['id'] = "tree_{}".format(model_name)
    field = add_sub_element(record, 'field', 'tree_{}'.format(model_name))
    field.attrib['name'] = 'name'
    field = add_sub_element(record, 'field', model_name)
    field.attrib['name'] = 'model'
    field = add_sub_element(record, 'field')
    field.attrib['name'] = 'arch'
    field.attrib['type'] = 'xml'
    tree = add_sub_element(field, 'tree')
    tree.attrib['string'] = model_name
    for fld_name in field_list:
        field = add_sub_element(tree, 'field')
        field.attrib['name'] = fld_name

    # 2. create form view
    record = add_sub_element(data, 'record')
    record.attrib['model'] = "ir.ui.view"
    record.attrib['id'] = "form_{}".format(model_name)
    field = add_sub_element(record, 'field', 'form_{}'.format(model_name))
    field.attrib['name'] = 'name'
    field = add_sub_element(record, 'field', model_name)
    field.attrib['name'] = 'model'
    field = add_sub_element(record, 'field')
    field.attrib['name'] = 'arch'
    field.attrib['type'] = 'xml'
    form = add_sub_element(field, 'form')
    form.attrib['string'] = model_description
    sheet = add_sub_element(form, "sheet")
    group = add_sub_element(sheet, 'group')
    for fld_name in field_list:
        field = add_sub_element(group, 'field')
        field.attrib['name'] = fld_name

    # 3. create search view
    record = add_sub_element(data, 'record')
    record.attrib['model'] = "ir.ui.view"
    record.attrib['id'] = "search_{}".format(model_name)
    field = add_sub_element(record, 'field', 'search_{}'.format(model_name))
    field.attrib['name'] = 'name'
    field = add_sub_element(record, 'field', model_name)
    field.attrib['name'] = 'model'
    field = add_sub_element(record, 'field')
    field.attrib['name'] = 'arch'
    field.attrib['type'] = 'xml'
    search = add_sub_element(field, 'search')
    for fld_name in field_list:
        field = add_sub_element(tree, 'field')
        field.attrib['name'] = fld_name

    # 4. create action
    record = add_sub_element(data, 'record')
    record.attrib['model'] = "ir.actions.act_window"
    record.attrib['id'] = "action_{}".format(model_name)
    field = add_sub_element(record, 'field', model_description)
    field.attrib['name'] = 'name'
    field = add_sub_element(record, 'field', format(model_name))
    field.attrib['name'] = 'model'
    field = add_sub_element(record, 'field', 'form')
    field.attrib['name'] = 'view_type'
    field = add_sub_element(record, 'field', 'tree,form')
    field.attrib['name'] = 'view_mode'
    field = add_sub_element(record, 'field')
    field.attrib['name'] = 'help'
    field.attrib['type'] = 'xml'
    p = add_sub_element(field, 'p', 'Create the first income type')
    p.attrib['class'] = "oe_view_nocontent_create"

    # create menu item
    menuitem = add_sub_element(data, 'menuitem')
    menuitem.attrib['id'] = 'menu_{}'.format(model_name)
    menuitem.attrib['name'] = model_description
    menuitem.attrib['sequence'] = "12" 
    menuitem.attrib['action'] = "action_{}".format(model_name)
    menuitem.attrib['parent'] = ""
  
    xml_string = etree.tostring(openerp, 
                               encoding='UTF-8', 
                               xml_declaration=True, 
                               pretty_print=True)
    
    filename = "{}.xml".format(model_name)
    # rezultat shranim na isti direktorij kot je py file
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, filename)
    try:
        with open(path, 'w') as fobj:
            fobj.write(xml_string)
    except (IOError, OSError) as exc:
        message = 'Unable to save file: %s' % exc
        raise UserError(message)

create_odoo_gui(model_name, field_list, model_description)











