import psycopg2
import json

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

# conn.autocommit = True
cursor = conn.cursor()
with open('api_data.json') as data_file:
    data = json.load(data_file)
    cursor.execute('''CREATE TABLE IF NOT EXISTS STATES(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT)
   ''')
    # sql = "INSERT INTO STATES (API,Description,Auth,HTTPS,Cors,Link,Category) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    # cursor.execute(sql, (json.dumps(data),))

    for d in data:
        sql = "INSERT INTO STATES (API,Description,Auth,HTTPS,Cors,Link,Category) VALUES(%s,%s,%s,%s,%s,%s,%s)", d)
        cursor

    print("has been inserted successfully")

    conn.commit()


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
#     insert_query = "INSERT INTO last VALUES (%s,%s,%s,%s,%s,%s,%s)"
#     cursor.execute(insert_query, tuple(my_data))
# #

# sql = '''CREATE TABLE US_TBLE(
#    API TEXT,
#    Description TEXT,
#    Auth TEXT,
#    HTTPS TEXT,
#    Cors TEXT,
#    Link TEXT,
#    Category TEXT
# );'''

# cursor.execute(sql)
# mycursor = conn.cursor()


# sql = "INSERT INTO US_TBLE (API,Description,Auth,HTTPS,Cors,Link,Category) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# val = [("Axolotl", "Collection of axolotl pictures and facts",".", "True", "yes", "https://theaxolotlapi.netlify.app/", "Animals"),
#        ("Cat Facts","Daily cat facts","","true","no","https://alexwohlbruck.github.io/cat-facts/","Animals"),
#        ("Cataas","Cat as a service (cats pictures and gifs)","","true","no","https://cataas.com/","Animals")]
#
# import json
# with open('api_data.json') as data_file:
#     data = json.load(data_file)
#     # for d in data:
    #     cursor.execute(sql, [d[0],d[1],d[2],d[3],d[4],d[5],d[6]])

#
# mycursor.executemany(sql, data)
# conn.commit()

# print((mycursor.rowcount, "record inserted"))


# import json
# with open('api_data.json') as data_file:
#     data = json.load(data_file)