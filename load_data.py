import psycopg2

"""Establishing the connection"""
conn = psycopg2.connect(
   database="universities", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)
"""Creating a cursor object using the cursor() method"""
cursor = conn.cursor()

"""Creating table as per requirement"""
sql ='''CREATE TABLE US_Universities(
   alpha_two_code TEXT,
   web_pages JSON,
   name TEXT,
   country TEXT,
   domains JSON,
   state_province TEXT 
)'''
cursor.execute(sql)
print("Table created successfully........")
conn.commit()