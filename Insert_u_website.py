import psycopg2
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

conn = psycopg2.connect(database=os.getenv('DATABASE'),
                        user=os.getenv('USER_HOST'),
                        password=os.getenv('PASSWORD'),
                        host=os.getenv('HOST'),
                        port=os.getenv('PORT')
                        )

conn.autocommit = True
cursor = conn.cursor()
"""to do Error Handling"""
sql ='''CREATE TABLE IF NOT EXISTS UNIVERSITIES_WEBSITE(
   alpha_two_code TEXT,
   web_pages JSONB,
   name TEXT,
   country TEXT,
   domains JSONB,
   state_province TEXT 
);'''

cursor.execute(sql)

with open('/home/ketter/Downloads/My_data.json', 'r') as m:
    json_data = json.load(m)

for d in json_data:
    alpha_two_code = d['alpha_two_code']
    web_pages = d['web_pages']
    name = d['name']
    country = d['country']
    domains = d['domains']
    state_province = d['state-province']

    values = ((alpha_two_code, json.dumps('web_pages'), name, country, json.dumps('domains'), state_province))
    sql = (f"INSERT INTO UNIVERSITIES_WEBSITE (alpha_two_code,web_pages,name,country,domains,state_province) "
           f"VALUES(%s,%s,%s,%s,%s,%s)")

    cursor.execute(sql, values)
    conn.commit()
