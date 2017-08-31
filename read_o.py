import sys
import re
import psycopg2

db_name='ozegov'
conn_string = "dbname='%s'" % db_name
conn = psycopg2.connect(conn_string)
conn.autocommit = True
pattern = '[,.:]'


def process_line(line):
    l = re.split(pattern, line, maxsplit=1)
    if len(l) == 2:
        word = l[0]
        description = l[1]
        if len(word) < 101:
            ssql = '''
            insert into ozegov (word, description)
            values(%(word)s, %(description)s)
            '''
            cursor = conn.cursor()
            cursor.execute(ssql, {'word': word, 'description': description})

i = 1
try:
    with open('/home/blaz/vimtest/ozegov') as fh:
        for line in fh:
            i += 1
            print i
            process_line(line)
            if i > 400:
                break
except EnvironmentError as err:
    print(err)

