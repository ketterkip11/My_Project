import psycopg2
"""Establishing the connection"""
conn = psycopg2.connect(
    database = "postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432"
)
conn.autocommit = True

"""Creating a cursor object using the cursor() method
"""
cursor = conn.cursor()

"""Preparing query to create a database"""
sql = '''CREATE database Universities''';

"""creating Database"""
cursor.execute(sql)
print("Database Created Succesfully....")