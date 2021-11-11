import json
import psycopg2

# json_data = open("data.csv").read()
# json_obj = json.loads(json_data)
# con = psycopg2.connect(database="universities", user='postgres', password='postgres', host='127.0.0.1', port= '5432')
# cursor = con.cursor()
#
# for item in json_obj:
#     API = item.get("API")
#     Description = item.get("Description")
#     Auth = item.get("Auth")
#     HTTPS = item.get("HTTPS")
#     Cors = item.get("Cors")
#     Link = item.get("Link")
#     Category = item.get("Category")
#     cursor.execute("insert into api1(API,Description,Auth,HTTPS,Cors,Link,Category) value(%s,%s,%s,%s,%s,%s,%s)",(API,Description,Auth,HTTPS,Cors,Link,Category))
# con.commit()
# con.close()
# """"""
# from mysql.connector import MySQLConnection, Error
# from python_mysql_dbconfig import read_db_config
#
# def insert_book(title, isbn):
#     query = "INSERT INTO books(title,isbn) " \
#             "VALUES(%s,%s)"
#     args = (title, isbn)
#
#     try:
#         db_config = read_db_config()
#         conn = MySQLConnection(**db_config)
#
#         cursor = conn.cursor()
#         cursor.execute(query, args)
#
#         if cursor.lastrowid:
#             print('last insert id', cursor.lastrowid)
#         else:
#             print('last insert id not found')
#
#         conn.commit()
#     except Error as error:
#         print(error)
#
#     finally:
#         cursor.close()
#         conn.close()
#
# def main():
#    insert_book('A Sudden Light','9781439187036')
#
# if __name__ == '__main__':
#     main()


# """"""
#
# from psycopg2 import MySQLConnection, Error
# from python_mysql_dbconfig import read_db_config
#
# def insert_books(books):
#     query = "INSERT INTO books(title,isbn) " \
#             "VALUES(%s,%s)"
#
#     try:
#         db_config = read_db_config()
#         conn = MySQLConnection(**db_config)
#
#         cursor = conn.cursor()
#         cursor.executemany(query, books)
#
#         conn.commit()
#     except Error as e:
#         print('Error:', e)
#
#     finally:
#         cursor.close()
#         conn.close()
#
# def main():
#     books = [('Harry Potter And The Order Of The Phoenix', '9780439358071'),
#              ('Gone with the Wind', '9780446675536'),
#              ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
#     insert_books(books)
#
# if __name__ == '__main__':
#     main()


data = ('/home/ketter/PycharmProjects/pythonProject1/api_data.json')
for d in data:
    print(d)


