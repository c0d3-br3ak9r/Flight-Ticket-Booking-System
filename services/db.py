from mysql.connector import connect, Error
import os

''' Import environment variables declared in .env file '''
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASS = os.environ.get("MYSQL_PASS")
MYSQL_DB_NAME = os.environ.get("MYSQL_DB_NAME")

class DB:
    def __init__(self):
        try:
            self.conn = connect(
                host=MYSQL_HOST,
                user=MYSQL_USER,
                password=MYSQL_PASS,
                database=MYSQL_DB_NAME)
            self.cursor = self.conn.cursor()
        except Error as e:
            print("DB ERROR :", e)
            self.conn = None

    def getall(self):
        self.cursor.execute("SELECT * FROM admin_users")
        res = self.cursor.fetchall()
        for i in res:
            print(i)

    ''' Get the hashed password of the admin user based on username '''
    def get_admin_password(self, username):
        query = "SELECT password FROM admin_users WHERE username=%s"
        self.cursor.execute(query, (username, ))
        res = self.cursor.fetchone()
        return res[0] if res else None
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()