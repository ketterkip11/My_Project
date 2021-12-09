import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

"""Establishing the connection"""
conn = psycopg2.connect(database=os.getenv('DATABASE'),
                        user=os.getenv('USER_HOST'),
                        password=os.getenv('PASSWORD'),
                        host=os.getenv('HOST'),
                        port=os.getenv('PORT')
                        )
"""Creating a cursor object using the cursor() method"""
cursor = conn.cursor()

"""Creating table as per requirement"""
sql ='''CREATE TABLE IF NOT EXISTS API(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()
#
# with open('data.csv', 'r') as f:
#    next(f)
#
#    cursor.copy_from(f, 'data.csv', sep=',')
#    conn.commit()
#
#    conn.close()
#
# f.close()

