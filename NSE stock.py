
class Dog:
    species = "canis familiaris"

    def __init__(self, name , age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    #instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"
#
    #another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass
class Dachshund():
    pass
class Bulldog():
    pass


#
# miles = Dog("Miles", 4)

# print(miles.description())
# print(miles.speak("Bow Wow"))

# print(miles)
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(buddy.speak("yap"))
print(buddy)








    # pass
# empl_1 = Employee()
# empl_2 = Employee()

# print(empl_1)
# print(empl_1)

# empl_1.first = 'alfred'
# empl_1.last = 'ketter'
# empl_1.email = 'alfred.ketter@company.com'
# empl_1.pay = 60000
#
# empl_2.first = 'george'
# empl_2.last = 'kibichii'
# empl_2.email = 'george.kibichii@company.com'
# empl_2.pay = 120000
#
# print(empl_1.email)
# print(empl_2.email)
""""""""""""""""""""""""""""""""""""""""""""
import pymysql

class DBHelper:

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = ""
        self.db = "emp"

    def __connect__(self):
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()


        """""""""""""""""""""""""""""""""""""""""
        
        import mysql.connector
        import time
        import config
        import HTMLParser
        import StringIO

        html_parser = HTMLParser.HTMLParser()

        try:
            connection = mysql.connector.connect( user=config.DB_USER, password=config.DB_PASSWORD,
                host = config.DB_HOST, database=config.DB_DATABASE, unix_socket=config.UNIX_SOCKET)

            cursor = connection.cursor()

        except mysql.connector.Error as err:
            logger.log('Database connection failed for '+config.DB_USER+'@'+config.DB_HOST+'/'+config.DB_DATABASE)
            exit()

        def get_bad_words():
            sql = ("SELECT word FROM word_blacklist")
            results = execute(sql)
            return results

        def get_moderation_method():
            sql = ("SELECT var_value FROM settings "
            "WHERE var_key = %(key)s")
            results = execute(sql, True, {'key':'moderation_method'})
            return results[0]

        def current_events():
            sql = ("SELECT count(id) FROM events WHERE event_date >= DATE_SUB(NOW(), INTERVAL 2 hour) AND event_date <= DATE_ADD(NOW(), INTERVAL 5 hour)")
            results = execute(sql, True)
            return results[0]

        def insert_social_post(channel, filter_type, post_id, validate, user_name, user_id, user_profile_picture, text, post_date, image_url, state):
            try:
                san_user_name = html_parser.unescape(user_name.encode('utf-8').strip()).decode("utf8").encode('ascii','ignore')
            except:
                san_user_name = html_parser.unescape(user_name.strip())
            try:
                san_text = html_parser.unescape(text.encode('utf-8').strip()).decode("utf8").encode('ascii','ignore')
            except:
                san_text = html_parser.unescape(text.strip())

            insert_post = ("INSERT IGNORE INTO social_posts "
                "(channel, filter_type, post_id, validate, user_name, user_id, user_profile_picture, text, post_date, image_url, state)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            execute(insert_post, False, [channel, filter_type, str(post_id), validate,
                san_user_name.strip(), user_id, user_profile_picture, san_text.strip(), post_date, image_url, state], True)

        def delete_posts(ids):
            fmt = ','.join(['%s'] * len(ids))
            cursor.execute("DELETE FROM `social_posts` WHERE id IN (%s)" % fmt,
                            tuple(ids))
            connection.commit()

        def update_campaigns(campaigns):
            sql = ("UPDATE social_campaigns "
                "SET last_updated = NOW()"
                "WHERE id IN ("+(','.join(str(c) for c in campaigns))+")")
            execute(sql, False, None, True)

        def execute(tuple, single = False, args = {}, commit = False):
            cursor.execute(tuple, args)

            if commit == True:
                connection.commit()
            else:
                if single == True:
                    return cursor.fetchone()
                else:
                    return cursor.fetchall()

        def lastrowid():
            return cursor.lastrowid

        def close():
            connection.close()
        
        """""""""""""""""""""""""""

        # class Database:
        #
        #     dbc = ("DATABASE", "USER_HOST", "PASSWORD", "HOST", "PORT")
        #
        #     def __int__(self):
        #         db = psycopg2.connect(*self.dbc)
        #         self.cursor = db.cursor()
        #
        #
        #     def create_table(self, sql):
        #         sql = ('CREATE TABLE IF NOT EXISTS NEW_TABLE(API TEXT,Description TEXT,Auth TEXT,HTTPS TEXT,Cors TEXT,Link TEXT,Category TEXT')
        #         return self.cursor.execute(sql)
        #

        #
        # def query (self, sql, params=None):
        #     sql.cursor.execute(sql,params or ())
        #     return self.fetchall()

        # with Database('DATABASE') as db:
        #     db.execute('CREATE TABLE IF NOT EXISTS NEW_TABLE(API TEXT,Description TEXT,Auth TEXT,HTTPS TEXT,Cors TEXT,Link TEXT,Category TEXT')
        #     db.execute('f"INSERT INTO NEW_TABLE (API,Description,Auth,HTTPS,Cors,Link,Category)'
        #                'f"VALUES(%s,%s,%s,%s,%s,%s,%s)')

        #
        # def __init__(self, connection_string=os.getenv['conn']):
        #     self.connection_string = connection_string
