#Simple Script updates database using psycopg2 and prints out data

import psycopg2
#connects to localhost 5432
conn = psycopg2.connect("dbname=test user=postgres password=ducati009 host=localhost")
cur = conn.cursor()

#Print existing data to console
result = cur.execute("SELECT id, num, data FROM test;")
rows = cur.fetchall()
for row in rows:
    print(row)

#Collect data from user keyboard input
value1 = raw_input("Enter a Number 1: ")
value2 = raw_input("Enter Value 2: ")

#insert data into postgresql
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(value1, value2))
# Make the changes to the database persistent
conn.commit()

result = cur.execute("SELECT id, num, data FROM test;")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close communication with the database
cur.close()
conn.close()
print "Script complete"
