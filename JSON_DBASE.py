# import psycopg2
#
# conn = psycopg2.connect(database="universities",
#                         user='postgres', password='postgres',
#                         host='127.0.0.1', port='5432'
#                         )
#
# conn.autocommit = True
# cursor = conn.cursor()
#
# sql = '''CREATE TABLE IF NOT EXISTS test121(
#    API TEXT,
#    Description TEXT,
#    Auth TEXT,
#    HTTPS TEXT,
#    Cors TEXT,
#    Link TEXT,
#    Category TEXT
# );'''
#
# # cursor.execute(sql)
# mycursor = conn.cursor()
# # sql = "INSERT INTO US_TBLE (API,Description,Auth,HTTPS,Cors,Link,Category) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# # val = [("Axolotl", "Collection of axolotl pictures and facts",".", "True", "yes", "https://theaxolotlapi.netlify.app/", "Animals"),
# #        ("Cat Facts","Daily cat facts","","true","no","https://alexwohlbruck.github.io/cat-facts/","Animals"),
# #        ("Cataas","Cat as a service (cats pictures and gifs)","","true","no","https://cataas.com/","Animals")]
# #
# #
# # mycursor.executemany(sql, val)
# # conn.commit()
# #
# # print((mycursor.rowcount, "record inserted"))
#
# data = []
# with open('/home/ketter/PycharmProjects/pythonProject1/api_data.json') as f:
#     for line in f:
#         data.append(json.loads(line))
#
# fields = [
#     "API"
#     "Description"
#     "Auth"
#     "HTTPS"
#     "Cors"
#     "Link"
#     "Category"
# ]
#
# for item in data:
#     my_data = [item[field] for field in fields]
#     for i, v in enumerate(my_data):
#         if isinstance(v,dict):
#             my_data[i] = json.dumps(v)
#     insert_query = "INSERT INTO test12 VALUES (%s,%s,%s,%s,%s,%s,%s)"
#     cursor.execute(insert_query, tuple(my_data))
#

import psycopg2

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS api(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT
);'''


cursor.execute(sql)

sql = ("INSERT INTO api "
       "(API, Description, Auth, HTTPS, Cors, Link, Category)" 
       "VALUES (%(API)s, %(Description)s, %(Auth)s, %(HTTPS)s, %(Cors)s, %(Link)s, %(Category)s)")
data = []
with open('/home/ketter/PycharmProjects/pythonProject1/api_data.json', 'r') as f:
    next(f)


api_data = {
     'API':'Cat Facts',
     'Description':'Daily cat facts',
     'Auth':'.',
     'HTTPS':'true',
     'Cors':'no',
     'Link':'https://alexwohlbruck.github.io/cat-facts/',
     'Category':'Animals',
    }

# cursor.execute(sql, api_data)
cursor.execute(sql, api_data)
conn.commit()

# cursor.commit()
