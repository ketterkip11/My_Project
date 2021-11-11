

import psycopg2
import json

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

# conn.autocommit = True
cursor = conn.cursor()



# cursor.execute("SELECT * FROM api2021")
# rows = cursor.fetchall()
#
# rowarray_list = []
# for row in rows:
#     t = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
# rowarray_list.append(t)
#
# j = json.dumps(rowarray_list)
# data = [{
#     "API":"Axolotl",
#     "Description":"Collection of axolotl pictures and facts",
#     "Auth":".",
#     "HTTPS":"True",
#     "Cors":"yes",
#     "Link":"https://theaxolotlapi.netlify.app/",
#     "Category":"Animals"
#     },
#     {
#     "API":"me",
#     "Description": "Collection of axolotl pictures and facts",
#     "Auth": ".",
#     "HTTPS": "True",
#     "Cors": "yes",
#     "Link": "https://theaxolotlapi.netlify.app/",
#     "Category": "Animals"
# }]

with open('api_data.json') as data_file:
    data = json.load(data_file)

sql = (f"INSERT INTO api2021 (API,Description,Auth,HTTPS,Cors,Link,Category) VALUES(%s,%s,%s,%s,%s,%s,%s)")

values = list([(d['API'],
                d['Description'],
                d['Auth'], d['HTTPS'],
                d['Cors'], d['Link'],
                d['Category'])
                for d in data])

cursor.executemany(sql, values)
conn.commit()




