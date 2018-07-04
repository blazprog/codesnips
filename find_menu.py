import sys
import psycopg2
from datetime import datetime

def main(argv):
    db_name = argv[1]
    menu_name = argv[2] + '%'
    # conn_string = "dbname='%s'" % "mmsfr"
    conn_string = "dbname='%s'" % db_name
    conn = psycopg2.connect(conn_string)
    ssql = """
        SELECT IUM.sequence, IUM.name,  IMD.name AS odoo_name, IMDP.name AS parent_name, IMD.module
        FROM ir_ui_menu IUM 
        INNER JOIN ir_model_data IMD ON IMD.res_id  = IUM.id 
        INNER JOIN ir_model_data IMDP ON IMDP.res_id  = IUM.parent_id
        WHERE IMD.model = 'ir.ui.menu' AND IMDP.model = 'ir.ui.menu'
        AND IUM.name LIKE %(menu_name)s;
    """
    cursor = conn.cursor()
    cursor.execute(ssql, {'menu_name': menu_name})
    records = cursor.fetchall()
    i = 1
    for sequence, name, odoo_name, parent_name, module in records:
        print "Menu".format(i)
        print "Name => ", name
        print "Odoo name => ", odoo_name
        print "Parent name => ", parent_name
        print "Sequence => ", sequence
        print "Module => ", module
        print "=" * 50
        print
        i += 1

if __name__ == '__main__':
    for arg in sys.argv:
        print arg
    main(sys.argv)
