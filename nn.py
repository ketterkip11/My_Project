import psycopg2

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS test")

sql = '''CREATE TABLE test(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT
);'''


sql = "INSERT INTO test (API,Description,Auth,HTTPS,Cors,Link,Category) VALUES(%s,%s,%s,%s,%s,%s,%s)"

api_data= {
         "API":"Cat Facts",
         "Description":"Daily cat facts",
         "Auth":"",
         "HTTPS":"true",
         "Cors":"no",
         "Link":"https://alexwohlbruck.github.io/cat-facts/",
         "Category":"Animals"
      }

# value = [(
#     api_data['API'],
#     api_data["Description"],
#     api_data["Auth"],
#     api_data["HTTPS"],
#     api_data["Cors"],
#     api_data["Link"],
#     api_data["Category"]
#
# )]
for x in api_data:
    cursor.executemany(sql, x)
# cursor.executemany(sql, api_data)
conn.commit()

