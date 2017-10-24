import sys
import os
import re

def pattern_exists(file_name, pattern):
    try:
        with open(file_name) as fh:
            for i, line in enumerate(fh):
                if pattern.search(line):
                    print file_name, line, i
    except EnvironmentError as err:
        print(err)

    return False

def search_in_files(dir_name, pattern, whitespaces=3):
    try:
        for obj in os.listdir(dir_name):
            new_obj = os.path.join(dir_name, obj)
            if os.path.isdir(new_obj):
                search_in_files(new_obj, pattern, whitespaces+3)
            else:
                fn, ext = os.path.splitext(new_obj)
                if ext == '.py':
                    pattern_exists(new_obj, pattern)
                    
    except OSError as e:
        print 'Non existing directory or missing rights'
        print e


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage => searchpy.py <model name>'
        sys.exit()

    model_name = sys.argv[1].replace('.', '\.')
    dir_name = '/home/blaz/projekti/odoo/'
    search_code = r"""
        (_name|_inherit)  # definiram model ali inheritam
        \s*               # nic ali vec presledkov
        =                 # enacaj
        \s*               # nic ali vec presledkov
        ['"]              # dvojni ali enojni narekovaj 
        %s                # ime modula 
        ['"]              # dvojni ali enojni narekovaj
    """ % model_name

    pattern = re.compile(search_code, re.VERBOSE)
    search_in_files(dir_name, pattern)
