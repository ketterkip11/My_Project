import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())




class Database:

    def __init__(self, database = 'universities', user='postgres', password='postgres', host='127.0.0.1', port='5432'):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port


    def connect(self):
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
        self.cursor = self.conn.cursor()
        return "database successfully connected"



    def create_table(self):
        self.connect()
        sql = '''CREATE TABLE IF NOT EXISTS NEW_TABLE(API TEXT,Description TEXT,Auth TEXT,HTTPS TEXT,Cors TEXT,Link TEXT,Category TEXT);'''
        result = self.cursor.execute(sql)
        # result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        self.connect()
        self.cursor.execute(sql)

print(Database().connect())
print(Database().create_table())

