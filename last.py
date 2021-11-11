import psycopg2
import json

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()
"""to do Error Handling"""
sql ='''CREATE TABLE IF NOT EXISTS DETAILS(
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
    d['state_province'] = d.pop('state-province')
    json_data = json_data
# print(json_data)

dict = {
    'alpha_two_code'
    'web_pages'
    'name'
    'country'
    'domains'
    'state_province'
}

alpha_two_code = dict['alpha_two_code']
web_pages = dict['web_pages']
name = dict['name']
country = dict['country']
domains = dict['domains']
state_province = dict['state_province']



# values = ((alpha_two_code, web_pages, name, country, domains, state_province) for d in json_data)


sql = (f"INSERT INTO details (alpha_two_code,web_pages,name,country,domains,state_province) VALUES(%s,%s,%s,%s,%s,%s,to_timestamp(%s))")

values = list([(d['alpha_two_code'], d['web_pages'], d['name'], d['country'], d['domains'], d['state_province']) for d in json_data])



cursor.executemany(sql, values)
conn.commit()

