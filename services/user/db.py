import sqlite3
import os

class UserDB:

    create_user_table = '''
                            CREATE TABLE IF NOT EXISTS `users` (
                                `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `username` TEXT NOT NULL UNIQUE,
                                `password` TEXT NOT NULL
                            )
                            '''

    create_user_session_table = '''
                                CREATE TABLE IF NOT EXISTS `user_session` (
                                    `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `user_id` INTEGER NOT NULL UNIQUE,
                                    `session_key` TEXT NOT NULL UNIQUE,
                                    `expires_at` DATETIME NOT NULL,
                                    CONSTRAINT `sess_user_id_fk` 
                                    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
                                )
                                '''
    
    enforce_foreign_key = "PRAGMA foreign_keys = ON;"


    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.dirname(os.path.abspath(__name__)) + "\\Flight-Ticket-Booking-System\\models\\flight_ticket_booking_database.db")
            self.cursor = self.conn.cursor()
            self.__exec(self.create_user_table)
            self.__exec(self.create_user_session_table)
            self.__exec(self.enforce_foreign_key)
        except sqlite3.Error as e:
            print("DB ERROR :", e)
            self.conn = None


    def getall(self):
        query = "SELECT * FROM `users`"
        self.__exec(query)
        res = self.cursor.fetchall()
        for i in res:
            print(i)


    ''' Create a new user '''
    def create_user(self, username, password):
        query = ''' INSERT INTO `users` (`username`, `password`) VALUES (?, ?) '''
        return self.__exec(query, [username, password])


    ''' Get the hashed password of the user based on username '''
    def get_user_password(self, username):
        query = "SELECT `id`, `password` FROM `users` WHERE `username`=?"
        self.__exec(query, [username])
        res = self.cursor.fetchone()
        return res if res else None
    

    ''' Get user id and expires at if there already exists a session with same key '''
    def get_user_id_expires(self, session_key):
        query = "SELECT `user_id`, `expires_at` FROM `user_session` WHERE `session_key`=?"
        self.__exec(query, [session_key])
        res = self.cursor.fetchone()
        return res
    

    ''' Delete session key if the user already has session '''
    def delete_session(self, session_id):
        query = "DELETE FROM `user_session` WHERE `session_key`=?"
        return self.__exec(query, [session_id])


    ''' Creates a new user session with session key and expires at as 24hr interval '''
    def create_session(self, user_id, session_key, expires_at):
        query = '''INSERT INTO `user_session` (`user_id`, `session_key`, `expires_at`)
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