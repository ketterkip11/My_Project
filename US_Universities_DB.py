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
conn.autocommit = True

"""Creating a cursor object using the cursor() method"""
cursor = conn.cursor()

"""Preparing query to create a database"""
sql = '''CREATE database Universities''';

"""creating Database"""
cursor.execute(sql)
print("Database Created Succesfully....")