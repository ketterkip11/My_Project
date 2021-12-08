import psycopg2

"""Establishing the connection"""
conn = psycopg2.connect(
   database="universities", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)
"""Creating a cursor object using the cursor() method"""
cursor = conn.cursor()

"""Creating table as per requirement"""
sql ='''CREATE TABLE APIz(
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

with open('data.csv', 'r') as f:
   next(f)

   cursor.copy_from(f, 'data.csv', sep=',')
   conn.commit()

   conn.close()

f.close()

