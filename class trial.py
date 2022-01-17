import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())




class Database:

    def __init__(self):
        self.database = 'universities'
        self.user = 'postgres'
        self.password = 'postgres'
        self.host = '127.0.0.1'
        self.port = 5432


    def __connect__(self):
        self.conn = psycopg2.connect(database=self.database, user=self.user, password=self.password, host=self.host, port=self.port)
        self.cursor = self.conn.cursor()
        return "database successfuly connected"



    def create_table(self):
        self.__connect__()
        sql = ('CREATE TABLE IF NOT EXISTS NEW_TABLE(API TEXT,Description TEXT,Auth TEXT,HTTPS TEXT,Cors TEXT,Link TEXT,Category TEXT')
        result = self.cursor.execute(sql)
        # result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cursor.execute(sql)
