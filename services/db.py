import sqlite3
import os

class DB:

    create_admin_table = '''
                            CREATE TABLE IF NOT EXISTS `admin_users` (
                                `id` int NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `username` varchar(20) NOT NULL UNIQUE,
                                `password` varchar(100) NOT NULL
                            )
                            '''

    create_admin_session_table = '''
                                CREATE TABLE IF NOT EXISTS `admin_session` (
                                    `id` int PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `admin_id` int NOT NULL UNIQUE,
                                    `session_key` varchar(100) NOT NULL UNIQUE,
                                    `expires_at` datetime NOT NULL,
                                    CONSTRAINT `sess_admin_id_fk` 
                                    FOREIGN KEY (`admin_id`) REFERENCES `admin_users` (`id`)
                                )
                                '''    

    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.dirname(os.path.abspath(__name__)) + "\\Flight-Ticket-Booking-System\\services\\flight_ticket_booking_database.db")
            self.cursor = self.conn.cursor()
            self.__exec(self.create_admin_table)
            self.__exec(self.create_admin_session_table)
        except sqlite3.Error as e:
            print("DB ERROR :", e)
            self.conn = None

    def getall(self):
        query = "SELECT * FROM admin_users"
        self.__exec(query)
        res = self.cursor.fetchall()
        for i in res:
            print(i)

    ''' Get the hashed password of the admin user based on username '''
    def get_admin_password(self, username):
        query = "SELECT id, password FROM admin_users WHERE username=?"
        self.__exec(query, [username])
        res = self.cursor.fetchone()
        return res if res else None
    
    ''' Checks whether there already exists a session with same key '''
    def session_exists(self, session_key):
        query = "SELECT user_id, expires_at FROM admin_session WHERE session_key=?"
        self.__exec(query, [session_key])
        res = self.cursor.fetchone()
        return res if res else None
    
    ''' Delete session key if the user already has session '''
    def delete_session(self, user_id):
        query = "DELETE FROM admin_session WHERE admin_id=?"
        self.__exec(query, [user_id])

    ''' Creates a new admin session with session key and expires at as 24hr interval '''
    def create_session(self, user_id, session_key, expires_at):
        query = '''INSERT INTO admin_session (admin_id, session_key, expires_at)
                VALUES (?, ?, ?)'''
        self.__exec(query, [user_id, session_key, expires_at])
        self.conn.commit()
    
    ''' Executes the SQL query '''
    def __exec(self, query, params=[]):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def __del__(self):
        self.cursor.close()
        self.conn.close()