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

cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS TEST")

sql = '''CREATE TABLE TEST(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT
);'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
