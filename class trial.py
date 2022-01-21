import json

import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())




class DatabaseConnector:

    def __init__(self):
        self.database = os.environ.get('DATABASE')
        self.user = os.environ.get('USER_HOST')
        self.password = os.environ.get('PASSWORD')
        self.host = os.environ.get('HOST')
        self.port = os.environ.get('PORT')



    def connection(self):
        conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
        cursor = conn.cursor()
        # cursor.execute(sql)
        # data = cursor.fetchall()
        # print("Db connection created")
        # print('cursor', type(cursor), cursor)
        return cursor, conn


    def create_table(self, sql):
        result, conn = self.connection()
        result.execute(sql)
        result1 = conn.commit()
        return result1

    def select_data(self):
        var_conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
        cursor = var_conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        return records

    def update_data(self):
        var_conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
        cursor = var_conn.cursor()
        cursor.execute(sql, vars=('kenya', 'web_pages', 'Moi University', 'africa', 'domains'))
        var_conn.commit()


    # def load_json(self):
    #     with open('api_data.json') as data_file:
    #         data = self.json.load(data_file)
    #     return data

    def insert_into_table(self):
        var_conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host,port=self.port)
        cursor = var_conn.cursor()

        with open('api_data.json') as data_file:
            data = json.load(data_file)

            for dict in data:
                API = dict['API']
                Description = dict['Description']
                Auth = dict['Auth']
                HTTPS = dict['HTTPS']
                Cors = dict['Cors']
                Link = dict['Link']
                Category = dict['Category']

                values = ((API, Description, Auth, HTTPS, Cors, Link, Category))

            cursor.execute(query_sql, values)
            data_results = var_conn.commit()
            return data_results

if __name__ == '__main__':
    sql = "CREATE TABLE IF NOT EXISTS NEW_TABLE(API TEXT,Description TEXT,Auth TEXT,HTTPS TEXT,Cors TEXT,Link TEXT,Category TEXT);"
    sql = 'SELECT * FROM public.universities_website'
    # query_sql = """INSERT INTO NEW_TABLE select * from json_populate_recordset(NULL::NEW_TABLE, %s); """
    query_sql = (f"INSERT INTO NEW_TABLE(API,Description,Auth,HTTPS,Cors,Link,Category) "
                f"VALUES(%s,%s,%s,%s,%s,%s,%s)")
    dbc = DatabaseConnector()
    # dbc.create_table(sql)
    dbc.select_data()
    dbc.insert_into_table()


