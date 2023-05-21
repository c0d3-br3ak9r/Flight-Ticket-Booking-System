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


    ''' Get all upcoming flights '''
    def get_all_flights(self):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) >= DATE('now')'''
        if ( self.__exec(query) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date '''
    def get_flights_date(self, date):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?)'''
        if ( self.__exec(query, [date]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date and time '''
    def get_flights_date_time(self, date, time):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) AND strftime('%H', `time`) >= ? '''
        if ( self.__exec(query, [date, time]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flight timing id '''
    def get_flight_timing_id(self, flight_no, date, time):
        query = ''' SELECT `id` FROM `flight_timings` WHERE
                    `flight_no`=? AND `date`=? AND `time`=? '''
        if ( self.__exec(query, [flight_no, date, time]) ):
            return self.cursor.fetchone()
        return -1


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
    

    ''' Delete existing flight '''
    def delete_flight(self, flight_no):
        query = "DELETE FROM `flights` WHERE `flight_no`=?"
        return self.__exec(query, [flight_no])
    

    ''' Delete all flight timings of particular flight '''
    def delete_flight_timing_from_flight(self, flight_no):
        query = "DELETE FROM `flight_timings` WHERE `flight_no`=?"
        return self.__exec(query, [flight_no])
    

    ''' Delete all flight timings at given date'''
    def delete_flight_timing_from_date(self, date):
        query = "DELETE FROM `flight_timings` WHERE `date`=?"
        return self.__exec(query, [date])
    

    ''' Delete all flight timings of particular flight at given date '''
    def delete_flight_timing_from_flight_date(self, flight_no, date):
        query = '''DELETE FROM `flight_timings` WHERE
                `flight_no`=? AND `date`=?'''
        return self.__exec(query, [flight_no, date])


    ''' Delete all flight timings of particular flight at given date on given time'''
    def delete_flight_timing_from_flight_date_time(self, flight_no, date, time):
        query = '''DELETE FROM `flight_timings` WHERE 
                `flight_no`=? AND `date`=? AND `time`=?'''
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