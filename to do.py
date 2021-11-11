import json

import psycopg2

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS API_TABLE3(
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

sql = (f"INSERT INTO API_TABLE3 (API,Description,Auth,HTTPS,Cors,Link,Category) "
       f"VALUES(%s,%s,%s,%s,%s,%s,%s)")


dict = {
    'API': "Axolotl",
    'Description': "Collection of axolotl pictures and facts",
    'Auth': ".",
    'HTTPS': "True",
    'Cors': "yes",
    'Link': "https://theaxolotlapi.netlify.app/",
    'Category': "Animals"
}

API = dict['API']
Description = dict['Description']
Auth = dict['Auth']
HTTPS = dict['HTTPS']
Cors = dict['Cors']
Link = dict['Link']
Category = dict['Category']


values = ((API, Description, Auth, HTTPS, Cors, Link, Category) for d in data)






# for value in data:
cursor.executemany(sql, values)


conn.commit()






