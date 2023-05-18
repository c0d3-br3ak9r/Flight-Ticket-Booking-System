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
        query = "SELECT id, password FROM admin_users WHERE username=%s"
        self.cursor.execute(query, (username, ))
        res = self.cursor.fetchone()
        return res if res else None
    
    ''' Checks whether there already exists a session with same key '''
    def session_exists(self, session_key):
        query = "SELECT user_id, expires_at FROM admin_session WHERE session_key=%s"
        self.cursor.execute(query, (session_key, ))
        res = self.cursor.fetchone()
        return res if res else None
    
    ''' Delete session key if the user already has session '''
    def delete_session(self, user_id):
        query = "DELETE FROM admin_session WHERE admin_id=%s"
        self.cursor.execute(query, (user_id, ))
        self.conn.commit()

    ''' Creates a new admin session with session key and expires at as 24hr interval '''
    def create_session(self, user_id, session_key, expires_at):
        query = '''INSERT INTO admin_session (admin_id, session_key, expires_at)
                VALUES (%s, %s, %s)'''
        self.cursor.execute(query, (user_id, session_key, expires_at))
        self.conn.commit()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()