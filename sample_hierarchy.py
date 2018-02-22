import psycopg2

category_names= ['A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J']
first_level = [100, 200, 300, 400, 500, 600, 700,800, 900]
second_level = [10, 20, 30, 40, 50, 60, 70, 80, 90]
third_level = [1, 2, 3, 4, 5, 6, 7, 8, 9]

conn_string = "dbname='sat'"
print ("Connecting to database\n	->%s" % (conn_string))
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
print ("Connected!")

ssql = """
        INSERT INTO PLACES (place, is_in) VALUES (%s,%s)
        """
for cn in category_names:
    for  fl in first_level:
        fl_name =  '{}{}'.format(cn, fl)
        for sl in second_level:
            sl_name = '{}{}'.format(cn, sl+fl)
            cursor.execute(ssql, (sl_name, fl_name))
            conn.commit()
            for tl in third_level:
                tl_name = '{}{}'.format(cn, fl+sl+tl)
                cursor.execute(ssql, (tl_name, sl_name))
                conn.commit()

cursor.close()
conn.close()
