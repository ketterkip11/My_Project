import psycopg2

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS api20(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT
);'''


cursor.execute(sql)

sql = ("INSERT INTO api20 "
       "(API, Description, Auth, HTTPS, Cors, Link, Category)" 
       "VALUES (%(API)s, %(Description)s, %(Auth)s, %(HTTPS)s, %(Cors)s, %(Link)s, %(Category)s)")

api_data = [{
     'API':"Axolotl",
     'Description':"Collection of axolotl pictures and facts",
     'Auth':".",
     'HTTPS':"True",
     'Cors':"yes",
     'Link':"https://theaxolotlapi.netlify.app/",
     'Category':"Animals",
    }]
# cursor.execute(sql, api_data)
cursor.executemany(sql, api_data)
conn.commit()

# cursor.commit()