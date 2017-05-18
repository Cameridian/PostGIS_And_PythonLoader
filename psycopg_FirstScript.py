#SIMPLE SCRIPT CALCULATES LENGTH OF ROADS IN Road_Centerline data
import psycopg2

try:
    conn = psycopg2.connect("dbname='test' user='postgres' port='5433' host='localhost' password='postgres'")
except:
    print "I am unable to connect to the database"
else:
    print "Connected to Database"

cur = conn.cursor()
cur.execute("""SELECT sum(ST_Length(wkb_geometry)) AS km_roads from road_centrelines""")
rows = cur.fetchall()
print "\nRows: \n"
for row in rows:
    print "  ", row[0]
