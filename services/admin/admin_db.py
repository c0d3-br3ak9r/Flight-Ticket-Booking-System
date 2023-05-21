import sqlite3
import os

class AdminDB:

    create_admin_table = '''
                            CREATE TABLE IF NOT EXISTS `admin_users` (
                                `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `username` TEXT NOT NULL UNIQUE,
                                `password` TEXT NOT NULL
                            )
                            '''

    create_admin_session_table = '''
                                CREATE TABLE IF NOT EXISTS `admin_session` (
                                    `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `admin_id` INTEGER NOT NULL UNIQUE,
                                    `session_key` TEXT NOT NULL UNIQUE,
                                    `expires_at` DATETIME NOT NULL,
                                    CONSTRAINT `sess_admin_id_fk` 
                                    FOREIGN KEY (`admin_id`) REFERENCES `admin_users` (`id`)
                                )
                                '''    
    
    enforce_foreign_key = "PRAGMA foreign_keys = ON;"


    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.dirname(os.path.abspath(__name__)) + "\\Flight-Ticket-Booking-System\\models\\flight_ticket_booking_database.db")
            self.cursor = self.conn.cursor()
            self.__exec(self.create_admin_table)
            self.__exec(self.create_admin_session_table)
            self.__exec(self.enforce_foreign_key)
        except sqlite3.Error as e:
            print("DB ERROR :", e)
            self.conn = None


    ''' Get the hashed password of the admin user based on username '''
    def get_admin_password(self, username):
        query = "SELECT id, password FROM admin_users WHERE username=?"
        if ( self.__exec(query, [username]) ):
            return self.cursor.fetchone()
        return -1
    

    ''' Checks whether there already exists a session with same key '''
    def session_exists(self, session_key):
        query = "SELECT expires_at FROM admin_session WHERE session_key=?"
        if ( self.__exec(query, [session_key]) ):
            return self.cursor.fetchone()
        return -1
    

    ''' Delete session key if the user already has session '''
    def delete_session(self, user_id):
        query = "DELETE FROM admin_session WHERE admin_id=?"
        return self.__exec(query, [user_id])


    ''' Creates a new admin session with session key and expires at as 24hr interval '''
    def create_session(self, user_id, session_key, expires_at):
        query = '''INSERT INTO admin_session (admin_id, session_key, expires_at)
                VALUES (?, ?, ?)'''
        return self.__exec(query, [user_id, session_key, expires_at])
    

    ''' Executes the SQL query '''
    def __exec(self, query, params=[]):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return 1
        except sqlite3.Error as e:
            print(e)
            return 0

    def __del__(self):
        self.cursor.close()
        self.conn.close()