from models.db import DB

class BookingDB(DB):

    create_booking_table = '''
                            CREATE TABLE IF NOT EXISTS `bookings` (
                                `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `booked_by_user_id` INTEGER NOT NULL,
                                `flight_timing_id` INTEGER NOT NULL,
                                `total_price` INTEGER NOT NULL,
                                CONSTRAINT `booked_by_user_id_fk` FOREIGN KEY(`booked_by_user_id`)
                                REFERENCES `users`(`id`),
                                CONSTRAINT `booking_flight_timing_id_fk` FOREIGN KEY(`flight_timing_id`)
                                REFERENCES `flight_timings`(`id`)
                            )
                            '''
    
        
    create_user_details_table = '''
                            CREATE TABLE IF NOT EXISTS `user_details` (
                                `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                `name` TEXT NOT NULL UNIQUE,
                                `age` INTEGER NOT NULL,
                                `gender` TEXT NOT NULL,
                                `booking_id` INTEGER NOT NULL,
                                `seat_no` TEXT NOT NULL,
                                `price` TEXT NOT NULL,
                                CONSTRAINT `user_details_booking_id_fk` 
                                    FOREIGN KEY (`booking_id`) REFERENCES `bookings`(`id`) ON DELETE CASCADE
                            )
                            '''


    def __init__(self):
        super().__init__()
        self._exec(self.create_booking_table)
        self._exec(self.create_user_details_table)


    def get_all_bookings(self):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`flight_timing_id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` '''
        if ( self._exec(query) ):
            return self.cursor.fetchall()
        return -1
    
    
    ''' Get all bookings of a particular user '''
    def get_all_bookings_from_user(self, user_id):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`flight_timing_id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `users`.`id` = ? '''
        if ( self._exec(query, [user_id]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get all bookings of a particular flight '''
    def get_all_bookings_from_flight(self, flight):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`flight_timing_id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flights`.`flight_no` = ? '''
        if ( self._exec(query, [flight]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get all bookings at given date '''
    def get_all_bookings_from_date(self, date):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`flight_timing_id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flight_timings`.`date` = ?'''
        if ( self._exec(query, [date]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get all bookings of a particular flight at given date '''
    def get_all_bookings_from_flight_date(self, flight, date):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`flight_timing_id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flights`.`flight_no` = ? AND `flight_timings`.`date` = ?'''
        if ( self._exec(query, [flight, date]) ):
            return self.cursor.fetchall()
        return -1


    ''' Get all bookings of a particular flight at given date and time '''
    def get_all_bookings_from_flight_date_time(self, flight, date, time):
        query = '''SELECT `bookings`.`id`, `username`, `flights`.`flight_no`, `source`,
                         `destination`, `airline`, `date`, `time`, `seat_no` 
                    FROM `users` INNER JOIN `bookings`
                    ON `bookings`.`user_id` = `users`.`id`
                    INNER JOIN `flight_timings` 
                    ON `bookings`.`flight_timing_id` = `flight_timings`.`id`
                    INNER JOIN `flights`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flights`.`flight_no` = ? AND `flight_timings`.`time` = ? 
                    AND `flight_timings`.`date` = ?'''
        if ( self._exec(query, [flight, time, date]) ):
            return self.cursor.fetchall()
        return -1


    ''' Create a new booking '''
    def create_booking(self, user_id, timing_id, price):
        print(user_id, timing_id, price)
        query = ''' INSERT INTO `bookings` (`booked_by_user_id`, `flight_timing_id`, `total_price`) 
                    VALUES (?, ?, ?) '''
        if ( self._exec(query, [user_id, timing_id, price]) ):
            return self.cursor.lastrowid
        return 0
    

    ''' Add user details with booking id '''
    def insert_user_details(self, details):
        query = ''' INSERT INTO `user_details` (`name`, `age`, `gender`, `seat_no`, `price`, `booking_id`) 
                    VALUES (?, ?, ?, ? ,?, ?) '''
        return self._execmany(query, details)
    

    ''' Get booked seats '''
    def get_booked_seats(self, flight_no, date, time):
        query = '''SELECT `seat_no` FROM `bookings`, `flight_timings`, `user_details` 
                   WHERE `bookings`.`flight_timing_id` = `flight_timings`.`id`
                   AND `bookings`.`id` = `user_details`.`booking_id`
                   AND `flight_timings`.`flight_no`=? AND `flight_timings`.`date`=?
                   AND `flight_timings`.`time`=? '''
        if ( self._exec(query, [flight_no, date, time]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Delete booking of flight'''
    def delete_booking(self, user_id, flight_timing_id):
        query = "DELETE FROM `bookings` WHERE `user_id`=? AND `flight_timing_id` = ?"
        return self._exec(query, [user_id, flight_timing_id])
    

    def __del__(self):
        return super().__del__()