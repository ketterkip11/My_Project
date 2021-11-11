# import pandas as pd
# from sqlalchemy import create_engine
# import json
# import psycopg2
#
# import pandas as pd
#
# # Data - Marks scored
# f = open('api_data.json', )
#
# data = json.load(f)
#
# pd.set_option('display.max_columns', None)
# df = pd.DataFrame.from_dict(data, orient='columns')
# data_F = df.to_string(index=False)
#
# alchemyEngine = create_engine(database="universities",
#                         user='postgres', password='postgres',
#                         host='127.0.0.1', port='5432');
#
# postgreSQLConnection = alchemyEngine.connect();
# # conn = psycopg2.connect(database="universities",
# #                         user='postgres', password='postgres',
# #                         host='127.0.0.1', port='5432'
# #                         )
# #
# # conn.autocommit = True
# # cursor = conn.cursor()
#
# postgreSQLTable = "frame";
#
# try:
#
#     frame1 = df.to_sql(postgreSQLTable, postgreSQLConnection, if_exists='fail');
#
# except ValueError as vx:
#
#     print(vx)
#
# except Exception as ex:
#
#     print(ex)
#
# else:
#
#     print("PostgreSQL Table %s has been created successfully." % postgreSQLTable);
#
# finally:
#
#     postgreSQLConnection.close();
import json

import pandas as pd
import psycopg2

conn = psycopg2.connect(database="universities",
                        user='postgres', password='postgres',
                        host='127.0.0.1', port='5432'
                        )

conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE IF NOT EXISTS api2022(
   API TEXT,
   Description TEXT,
   Auth TEXT,
   HTTPS TEXT,
   Cors TEXT,
   Link TEXT,
   Category TEXT
);'''

cursor.execute(sql)

f = open('api_data.json', )

# returns JSON object as
# a dictionary
data = json.load(f)

df = pd.DataFrame.from_dict(data, orient='columns')


def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    # cursor.close()
    for i in df.index:
        sql = """INSERT INTO api2022 "
               "(API, Description, Auth, HTTPS, Cors, Link, Category)
               "VALUES ('%s','%s','%s','%s','%s','%s','%s');
               """ % (i['API'], i['Descriptions'], i['Auths'], i['HTTPS'], i['Cor'], i['Link'], i['Category'])

    single_insert(conn, sql)

conn.close()
# print(df.head())

# with open('data_1.json') as file:
#     # change json.load(file) to file.read()
#     data = file.read()

#
# # Just put a placeholder %s instead of using {} and .format().
# query_sql = """
# insert into test1 select * from
# json_populate_recordset(NULL::test1, %s);
# """
#
# # change .execute(query_sql) to .execute(query_sql, (data,))
# cursor.execute(query_sql, (data,))
# # Add a commit on the connection.
# conn.commit()

# cursor.execute(sql)
#
# sql = ("INSERT INTO api20 "
#        "(API, Description, Auth, HTTPS, Cors, Link, Category)"
#        "VALUES (%(API)s, %(Description)s, %(Auth)s, %(HTTPS)s, %(Cors)s, %(Link)s, %(Category)s)")
#
# api_data = [{
#      'API':'Cat Facts',
#      'Description':'Daily cat facts',
#      'Auth':'.',
#      'HTTPS':'true',
#      'Cors':'no',
#      'Link':'https://alexwohlbruck.github.io/cat-facts/',
#      'Category':'Animals',
#     },


# # import csv
# # import psycopg2
# # conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
# # cur = conn.cursor()
# # with open('data.csv', 'r') as f:
# #     reader = csv.reader(f)
# #     next(reader) # Skip the header row.
# #     for row in reader:
# #         cur.execute(
# #         "INSERT INTO APIs(%s, %s, %s, %s)",
# #         row
# #     )
# # conn.commit()
# #
# # import psycopg2
# #
# # conn = psycopg2.connect(database="universities",
# #                         user='postgres', password='postgres',
# #                         host='127.0.0.1', port='5432'
# #                         )
#
# # conn.autocommit = True
# # cursor = conn.cursor()
# #
# # sql = '''CREATE TABLE TEST(
# #    API TEXT,
# #    Description TEXT,
# #    Auth TEXT,
# #    Cors TEXT,
# #    Link TEXT,
# #    Category TEXT
# # );'''
#
# # cursor.execute(sql)
#
# # sql2 = '''COPY data(API,Description,\
# # Auth,Cors,Link,Category)
# # FROM 'data.csv'
# # DELIMITER ','
# # CSV HEADER;'''
# #
# # cursor.execute(sql2)
# #
# # sql3 = '''select * from data;'''
# # cursor.execute(sql3)
# # for i in cursor.fetchall():
# #     print(i)
# #
# # conn.commit()
# # conn.close()
#
# # items = pickle.load(open(data.json, "rb"))
#
# """1st trial"""
# import json
# #
# # import psycopg2
# #
# # conn = psycopg2.connect(database="universities",
# #                         user='postgres', password='postgres',
# #                         host='127.0.0.1', port='5432'
# #                         )
# #
# # conn.autocommit = True
# # cursor = conn.cursor()
#
# # sql = '''CREATE TABLE IF NOT EXISTS test12(
# #    API TEXT,
# #    Description TEXT,
# #    Auth TEXT,
# #    HTTPS TEXT,
# #    Cors TEXT,
# #    Link VARCHAR,
# #    Category TEXT
# # );'''
# #
# # cursor.execute(sql)
#
# # # insert each csv row as a record in our database
# # with open("data.csv", 'r') as f:
# #     next(f)
# #     for row in f:
# #         cursor.execute("""
# #         INSERT INTO test1
# #         VALUES ('{}','{}','{}','{}','{}','{}','{}')
# #         """).format(
# #             row.split(",")[0],
# #             row.split(",")[1],
# #             row.split(",")[2],
# #             row.split(",")[3],
# #             row.split(",")[4],
# #             row.split(",")[5],
# #             row.split(",")[6]
# #         )
# #
# # cursor.commit()
#
#
# """2nd trial"""
#
#
# # import psycopg2
# # # connection = psycopg2.connect(connection_string)
# # cursor = conn.cursor()
# # cursor.execute("set search_path to public")
# #
# #
# # with open('data_1.json') as file:
# #     # change json.load(file) to file.read()
# #     data = file.read()
# #
# # # Just put a placeholder %s instead of using {} and .format().
# # query_sql = """
# # insert into test1 select * from
# # json_populate_recordset(NULL::test1, %s);
# # """
# #
# # # change .execute(query_sql) to .execute(query_sql, (data,))
# # cursor.execute(query_sql, (data,))
# # # Add a commit on the connection.
# # conn.commit()
#
# #
# # data = []
# # with open('/home/ketter/PycharmProjects/pythonProject1/api_data.json') as f:
# #     for line in f:
# #         data.append(json.loads(line))
# #
# # fields = [
# #     "API"
# #     "Description"
# #     "Auth"
# #     "HTTPS"
# #     "Cors"
# #     "Link"
# #     "Category"
# # ]
# #
# # for item in data:
# #     my_data = [item[field] for field in fields]
# #     for i, v in enumerate(my_data):
# #         if isinstance(v,dict):
# #             my_data[i] = json.dumps(v)
# #     insert_query = "INSERT INTO test12 VALUES (%s,%s,%s,%s,%s,%s,%s)"
# #     cursor.execute(insert_query, tuple(my_data))
#
#
# import json
# import pandas as pd
# import psycopg2
#
#
# # f = open('api_data.json', )
# #
# # data = json.load(f)
# #
# # pd.set_option('display.max_columns', None)
# # df = pd.DataFrame.from_dict(data, orient='columns')
# # data_F = df.to_string(index=False)
#
# # print(data_F)
#
#
# # INPUT YOUR OWN CONNECTION STRING HERE
# conn = psycopg2.connect(database="universities",
#                         user='postgres', password='postgres',
#                         host='127.0.0.1', port='5432'
#                         )
#
# conn.autocommit = True
# cursor = conn.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS last;")
# sql = '''CREATE TABLE last(
#    API TEXT,
#    Description TEXT,
#    Auth TEXT,
#    HTTPS TEXT,
#    Cors TEXT,
#    Link TEXT,
#    Category TEXT
# );'''
#
# cursor.execute(sql)
#
# data = []
# with open('/home/ketter/PycharmProjects/pythonProject1/api_data.json') as f:
#     for line in f:
#         data.append(json.loads(line))
#
# fields = [
#     "API"
#     "Description"
#     "Auth"
#     "HTTPS"
#     "Cors"
#     "Link"
#     "Category"
# ]
#
# for item in data:
#     my_data = [item[field] for field in fields]
#     # for i, v in enumerate(my_data):
#     #     if isinstance(v,dict):
#     #         my_data[i] = json.dumps(v)
#     insert_query = "INSERT INTO last VALUES (%s,%s,%s,%s,%s,%s,%s)"
#     cursor.execute(insert_query, tuple(my_data))
#
#     # cursor.execute("set search_path to public")
#     #
#     #
#     # with open('data_1.json') as file:
#     #     # change json.load(file) to file.read()
#     #     data = file.read()
#     #
#     # # Just put a placeholder %s instead of using {} and .format().
#     # query_sql = """
#     # insert into test1 select * from
#     # json_populate_recordset(NULL::test1, %s);
#     # """
#     #
#     # # change .execute(query_sql) to .execute(query_sql, (data,))
#     # cursor.execute(query_sql, (data,))
#     # # Add a commit on the connection.
#     # conn.commit()
#
# # def single_inserts(cursor, data_F, Frame):
# #     for i in data_F.index:
# #         cols  = ','.join(list(data_F.columns))
# #         vals  = [data_F.at[i,col] for col in list(data_F.columns)]
# #         query = "INSERT INTO Frame (API,Description,Auth,HTTPS,Cors,Link,Category) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# #         cursor.execute(query)
# #     print("single_inserts() done")
#
#
#
#
#
# import json
# with open('api_data.json') as data_file:
#     data = json.load(data_file)
#
# print(type(data))

import csv