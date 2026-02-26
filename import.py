import psycopg2

path = '/home/maso2/Desktop/python-projekte/dbStuff/testData.csv'
tableName = "testData"

conn = psycopg2.connect("dbname=test user=postgres password='2302' host=localhost")
cur = conn.cursor()

query = f"COPY {tableName} FROM '{path}' WITH (FORMAT csv, HEADER true);"
cur.execute(query)

conn.commit()
cur.close()
conn.close()
