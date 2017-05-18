#SCRIPT not complete needs work
from sys import argv
import psycopg2

try:
    conn = psycopg2.connect("dbname='test' user='postgres' port='5433' host='localhost' password='postgres'")
except:
    print "I am unable to connect to the database"
else:
    print "Connected to Database"

tablename = raw_input("Enter table name: ")
try:
    cur = conn.cursor()
    cur.execute("""SELECT sum(ST_Length(wkb_geometry)) AS km_roads from """ + tablename)
except:
    print "Error in SQL statment"
rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print "  ", row[0]
