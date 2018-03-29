# -*- coding: utf-8 -*-
import os
import sqlite3
import re

root_dir = "/home/blaz/projekti/odoo/mentis/addons-openerpsl/"

def write_dependencies(openerp_file, module_name,  db_cursor):
    '''
    Prebere openerp datoteko in zapise odvisnosti 
    :param file: __openerp__.file
    '''
    print('Dependencies for ', module_name)
    try:
        with open(openerp_file) as fh:
            reading_dependencies = False
            for line in fh:
                if 'depends' in line:
                    reading_dependencies = True
                    module_list = line.split(':')[1]
                    module_list = re.sub('[\[\]]', '', module_list)
                    for module in module_list.split(','):
                        module = re.sub('[\'\"]', '', module)
                        if module.strip():
                            print (module.strip())
                            sql = '''
                                INSERT INTO modul_dependencies VALUES("{}", "{}")
                            '''.format(module_name, module.strip())
                            print(sql)
                            c.execute(sql)
                            conn.commit()
                    if ']' in line:
                        reading_dependencies = False
                elif reading_dependencies:
                    module_list = re.sub('[\[\]]', '', line)
                    for module in module_list.split(','):
                        module = re.sub('[\'\"]', '', module)
                        if module.strip():
                            print (module.strip())
                            sql = '''
                                INSERT INTO modul_dependencies VALUES("{}","{}")
                            '''.format(module_name, module.strip())
                            print (sql)
                            c.execute(sql)
                            conn.commit()
                    if ']' in line:
                        reading_dependencies = False
    except EnvironmentError as env_err:
        print (env_err)

conn = sqlite3.connect('dependencies.db')
c = conn.cursor()
# c.execute('''
#     CREATE TABLE modul_dependencies(module text, depends_on text)
# ''')
for dir_name in os.listdir(root_dir):
    full_name = os.path.join(root_dir, dir_name)
    if os.path.isdir(full_name):
        for file in os.listdir(full_name):
            ful_file_name = os.path.join(full_name, file)
            if os.path.isfile(ful_file_name):
                if file == '__openerp__.py':
                    write_dependencies(ful_file_name, dir_name, c)

c.close()
