import sqlite3
import os

class BookingDB:

    create_booking_table = '''
                            CREATE TABLE IF NOT EXISTS `bookings` (
                                `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `user_id` INTEGER NOT NULL,
                                `flight_timing_id` INTEGER NOT NULL,
                                `seat_no` INTEGER NOT NULL,
                                CONSTRAINT `booking_user_id_fk` FOREIGN KEY(`user_id`)
                                REFERENCES `users`(`id`),
                                CONSTRAINT `booking_flight_timing_id_fk` FOREIGN KEY(`flight_timing_id`)
                                REFERENCES `flight_timings`(`id`)
                            )
                            '''
    
    
    enforce_foreign_key = "PRAGMA foreign_keys = ON;"


    def __init__(self):
        try:
            self.conn = sqlite3.connect(os.path.dirname(os.path.abspath(__name__)) + "\\Flight-Ticket-Booking-System\\models\\flight_ticket_booking_database.db")
            self.cursor = self.conn.cursor()
            self.__exec(self.create_booking_table)
            self.__exec(self.enforce_foreign_key)
        except sqlite3.Error as e:
            print("DB ERROR :", e)
            self.conn = None


    def get_all_bookings(self):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` '''
        self.__exec(query)
        return self.cursor.fetchall()
    
    ''' Get all bookings of a particular user '''
    def get_all_bookings_user(self, user_id):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `users`.`id` = ? '''
        self.__exec(query, [user_id])
        return self.cursor.fetchall()
    

    ''' Get all bookings of a particular flight '''
    def get_all_bookings_flight(self, flight):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flights`.`flight_no` = ? '''
        self.__exec(query, [flight])
        return self.cursor.fetchall()


    ''' Get all bookings of a particular flight on given time '''
    def get_all_bookings_flight_time(self, flight, time):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flights`.`flight_no` = ? AND `flight_timings`.`time` = ? '''
        self.__exec(query, [flight, time])
        return self.cursor.fetchall()


    ''' Create a new booking '''
    def create_booking(self, user_id, timing_id, seat_no):
        query = ''' INSERT INTO `bookings` (`user_id`, `flight_timing_id`, `seat_no`) 
                    VALUES (?, ?, ?) '''
        return self.__exec(query, [user_id, timing_id, seat_no])
    

    ''' Get booked seats '''
    def get_booked_seats(self, flight_no, date, time):
        query = '''SELECT `seat_no` FROM `bookings`, `flight_timings` 
                   WHERE `bookings`.`flight_timing_id` = `flight_timings`.`id`
                   AND `flight_timings`.`flight_no`=? AND `flight_timings`.`date`=?
                   AND `flight_timings`.`time`=? '''
        if ( self.__exec(query, [flight_no, date, time]) ):
            return self.cursor.fetchone()
        return -1
    

    ''' Delete booking of flight'''
    def delete_booking(self, user_id, flight_timing_id):
        query = "DELETE FROM `bookings` WHERE `user_id`=? AND `flight_timing_id` = ?"
        return self.__exec(query, [user_id, flight_timing_id])
    

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