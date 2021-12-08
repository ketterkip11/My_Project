import json
import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

conn = psycopg2.connect(database=os.getenv('DATABASE'),
                        user=os.getenv('USER_HOST'),
                        password=os.getenv('PASSWORD'),
                        host=os.getenv('HOST'),
                        port=os.getenv('PORT')
                        )

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS API_TABLE_NEW(
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
    # print(data)

for dict in data:

    API = dict['API']
    Description = dict['Description']
    Auth = dict['Auth']
    HTTPS = dict['HTTPS']
    Cors = dict['Cors']
    Link = dict['Link']
    Category = dict['Category']

    values = ((API, Description, Auth, HTTPS, Cors, Link, Category))

    sql = (f"INSERT INTO API_TABLE_NEW (API,Description,Auth,HTTPS,Cors,Link,Category) "
           f"VALUES(%s,%s,%s,%s,%s,%s,%s)")

    cursor.execute(sql, values)
    conn.commit()






