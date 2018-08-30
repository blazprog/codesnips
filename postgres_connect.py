import psycopg2

def main():
	#Define our connection string
	conn_string = "host='10.0.0.9' dbname='mm-prezentacija' user='odoo8' password='odoo8'"

    # peer authentication
	# conn_string = "dbname='sat'"

	print ("Connecting to database\n	->%s" % (conn_string))
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print ("Connected!")
 
if __name__ == "__main__":
	main()
