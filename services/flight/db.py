import sqlite3
import os

class FlightDB:

    create_flight_table = '''
                            CREATE TABLE IF NOT EXISTS `flights` (
                                `flight_no` TEXT NOT NULL PRIMARY KEY,
                                `airline` TEXT NOT NULL,
                                `source` TEXT NOT NULL,
                                `destination` TEXT NOT NULL
                            )
                            '''

    create_flight_timing_table = '''
                                CREATE TABLE IF NOT EXISTS `flight_timings` (
                                    `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `flight_no` TEXT NOT NULL,
                                    `date` DATE NOT NULL,
                                    `time` TIME NOT NULL,
                                    CONSTRAINT 'flight_no_timing_fk' FOREIGN KEY(`flight_no`) REFERENCES
                                    `flights`(`flight_no`) ON DELETE CASCADE
                                )
                                ''' 

    enforce_foreign_key = "PRAGMA foreign_keys = ON;"   

    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.dirname(os.path.abspath(__name__)) + "\\Flight-Ticket-Booking-System\\models\\flight_ticket_booking_database.db")
            self.cursor = self.conn.cursor()
            self.__exec(self.create_flight_table)
            self.__exec(self.create_flight_timing_table)
            self.__exec(self.enforce_foreign_key)
        except sqlite3.Error as e:
            print("DB ERROR :", e)
            self.conn = None


    def getall(self):
        query = "SELECT * FROM `flights`"
        self.__exec(query)
        res = self.cursor.fetchall()
        for i in res:
            print(i)

    
    ''' Checks whether there already exists a session with same key '''
    def session_exists(self, session_key):
        query = "SELECT `user_id`, `expires_at` FROM `admin_session` WHERE `session_key`=?"
        self.__exec(query, [session_key])
        res = self.cursor.fetchone()
        return res if res else None
    

    ''' Delete session key if the user already has session '''
    def delete_session(self, user_id):
        query = "DELETE FROM `admin_session` WHERE `admin_id`=?"
        self.__exec(query, [user_id])


    ''' Creates a new flight '''
    def create_flight(self, flight_no, airline, source, destination):
        query = '''INSERT INTO `flights` (`flight_no`, `airline`, `source`, `destination`)
        VALUES (?, ?, ?, ?)'''
        return self.__exec(query, [flight_no, airline, source, destination])
        

    ''' Creates a new flight timing '''
    def create_flight_timing(self, flight_no, date, time):
        query = '''INSERT INTO `flight_timings` (`flight_no`, `date`, `time`) VALUES
                    (?, ?, ?)'''
        return self.__exec(query, [flight_no, date, time])
        
    
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