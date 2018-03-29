import sys
import re
import psycopg2

db_name='ozegov'
conn_string = "dbname='%s'" % db_name
conn = psycopg2.connect(conn_string)
conn.autocommit = True
pattern = '[,.:]'


def insert_data():
    ssql = '''
    insert into test_insert(action, employee_id, action_desc, name)
    values(%(action)s, %(employee_id)s, %(action_desc)s, %(name)s)
    '''

    value1_dict = {"action": 'sign_in',
                  "employee_id": 1,
                  "action_desc" :'Redna prijava',
                  "name": '2018-03-02' }


    value2_dict = {"action": 'sign_out',
                  "employee_id": 1,
                  "action_desc" :'Redna prijava',
                  "name": '2018-03-03' }

    values = (value1_dict, value2_dict)
    cursor = conn.cursor()
    cursor.executemany(ssql, values)

if __name__ == '__main__':
    insert_data()

