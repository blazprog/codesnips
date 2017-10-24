import sys
import os
import re

def pattern_exists(file_name, pattern_id, pattern_inherit):
    try:
        with open(file_name) as fh:
            for i, line in enumerate(fh):
                if pattern_inherit.search(line):
                    print file_name, line.strip(), str(i)
                elif pattern_id.search(line):
                    print file_name, line.strip(), str(i)
    except EnvironmentError as err:
        print(err)

    return False

def search_in_files(dir_name, pattern_id, pattern_inherit, whitespaces=3):
    try:
        for obj in os.listdir(dir_name):
            new_obj = os.path.join(dir_name, obj)
            if os.path.isdir(new_obj):
                search_in_files(new_obj, pattern_id, pattern_inherit, whitespaces+3)
            else:
                fn, ext = os.path.splitext(new_obj)
                if ext == '.xml':
                    pattern_exists(new_obj, pattern_id, pattern_inherit)
                    
    except OSError as e:
        print 'Non existing directory or missing rights'
        print e


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage => searchpy.py <model name>'
        sys.exit()

    view_name = sys.argv[1].replace('.', '\.')
    dir_name = '/home/blaz/projekti/odoo/'

    search_code_inherit = r"""
        <field                     # zacetek
        \s+                        # eden ali vec presledkov
        name=['"]inherit_id['"]    # attribut name
        \s+                        # eden ali vec presledkoov
        ref=['"]                   # ref attribut     
        .*                         # opcijsko ime modula in pika
        %s                         # parameter za ime viewa, ki ga inheritam
        ['"]                       # enojni ali dvojni narekovaj
        />                         # zakljucni tag                       
    """ % view_name

    search_code_id = r"""
        \s+                             # eden ali vec presledkov 
        id=['"]                         # id
        %s                              # parameter za id viewa
        ['"]                            # enojni ali dvojni narekovaj 
    """ % view_name


    pattern_id = re.compile(search_code_id, re.VERBOSE)
    pattern_inherit = re.compile(search_code_inherit, re.VERBOSE)
    search_in_files(dir_name, pattern_id, pattern_inherit)
