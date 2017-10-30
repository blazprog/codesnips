import os

def print_dir(dir_name, whitespaces=3):
    try:
        for obj in os.listdir(dir_name):
            new_obj = os.path.join(dir_name, obj)
            if os.path.isdir(new_obj):
                print ' ' * whitespaces, new_obj
                print_dir(new_obj, whitespaces+3)
            else:
                print ' ' * whitespaces, os.path.basename(new_obj)
    except OSError as e:
        print 'Non existing directory or missing rights'
        print e


if __name__ == '__main__':
    D
    dir_name = '/home/blaz/projekti/odoo/mentis/addons-openerpsl/mentis_payroll'
    print dir_name
    print_dir(dir_name)
