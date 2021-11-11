import csv

import psycopg2
import json

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

# conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS API_DATA(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT
);'''


cursor.execute(sql)

with open('api_data.json') as data_file:
    data = json.load(data_file)

sql = (f"INSERT INTO API_DATA (API,Description,Auth,HTTPS,Cors,Link,Category) "
       f"VALUES(%s,%s,%s,%s,%s,%s,%s)")

values = list([(d['API'],
                d['Description'],
                d['Auth'],
                d['HTTPS'],
                d['Cors'],
                d['Link'],
                d['Category'])
               for d in data])

cursor.executemany(sql, values)

conn.commit()