# -*- coding: utf-8 -*-
import os

# print current working directory

def naredi_odoo_modul(module_name):
    work_dir = os.getcwd()
    module_dir = "{}/{}".format(work_dir, module_name)
    os.mkdir(module_dir)
    init_file = os.path.join(module_dir, '__init__.py')
    with open(init_file, 'w' ) as fobj:
        fobj.write("# -*- coding: utf-8 -*-\n")
        fobj.write("import models\n")
    open_erp_file = os.path.join(module_dir,'__openerp__.py')
    open_erp_list = [
        ('name' , 'Mentis  MODULE_NAME'),
        ('version' , '1.0'),
        ('author' , 'Mentis d.o.o'),
        ('website', 'http://www.odoo.si'),
        ('category', 'MODULE_CATEGORY'),
        ('description', '""" MODULE_DESCRIPTION """'),
        ('application' , False),
        ('depends', []),
        ('data', []),
        ('installable', True),
        ('active', False),
    ]
    with open(open_erp_file, 'w' ) as fobj:
        fobj.write("{\n")
        for key, value in open_erp_list:
            line = "'{}' :".format(key)
            if type(value) == str:
                line += "'{}'".format(value)
            elif type(value) in (bool, list):
                line += str(value)
            line += ','
            fobj.write(' ' * 4)
            fobj.write(line)
            fobj.write('\n')
        fobj.write("}\n")

    dirs = ['models', 'views', 'i18n']
    for d in dirs:
        os.mkdir("{}/{}".format(module_dir, d))
    pass

naredi_odoo_modul('mentis_mrp')