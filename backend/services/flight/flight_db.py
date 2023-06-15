from models.db import DB

class FlightDB(DB):

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
    
    create_flight_price_map_table = '''
                                CREATE TABLE IF NOT EXISTS `flight_price_map` (
                                    `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `flight_timing_id` INTEGER NOT NULL UNIQUE,
                                    `first_class_price` INTEGER NOT NULL,
                                    `business_class_price` INTEGER NOT NULL,
                                    `economy_class_price` INTEGER NOT NULL,
                                    CONSTRAINT 'flight_price_timing_id_fk' FOREIGN KEY(`flight_timing_id`) REFERENCES
                                    `flight_timings`(`id`) ON DELETE CASCADE
                                )
                                ''' 
    
    create_flight_seat_map_table = '''
                                CREATE TABLE IF NOT EXISTS `flight_seat_map` (
                                    `id` INTEGER NOT NULL PRIMARY KEY DEFAULT AUTO_INCREMENT,
                                    `flight_no` TEXT NOT NULL,
                                    `first_class_seat` INTEGER NOT NULL,
                                    `business_class_seat` INTEGER NOT NULL,
                                    `economy_class_seat` INTEGER NOT NULL,
                                    CONSTRAINT 'flight_seat_flight_no_fk' FOREIGN KEY(`flight_no`) REFERENCES
                                    `flights`(`flight_no`) ON DELETE CASCADE
                                )
                                ''' 


    def __init__(self):
        super().__init__()
        self._exec(self.create_flight_table)
        self._exec(self.create_flight_timing_table)
        self._exec(self.create_flight_price_map_table)
        self._exec(self.create_flight_seat_map_table)


    ''' Get all upcoming flights '''
    def get_all_flights(self):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`, `flight_timings`.`id`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) >= DATE('now') ORDER BY `date`, `time`'''
        if ( self._exec(query) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on flight '''
    def get_flights_from_flight(self, flight):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`, , `flight_timings`.`id`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flights`.`flight_no` = ? ORDER BY `date`, `time`'''
        if ( self._exec(query, [flight]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date '''
    def get_flights_from_date(self, date):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`, `flight_timings`.`id`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) ORDER BY `date`, `time`'''
        if ( self._exec(query, [date]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date of particular flight '''
    def get_flights_from_flight_date(self, flight, date):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`, `flight_timings`.`id`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) AND `flights`.`flight_no` = ? ORDER BY `date`, `time`'''
        if ( self._exec(query, [date, flight]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date and time '''
    def get_flights_from_date_time(self, date, time):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`, `flight_timings`.`id`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) AND strftime('%H', `time`) >= ? ORDER BY `date`, `time`'''
        if ( self._exec(query, [date, time]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date and time of particular flight'''
    def get_flights_from_flight_date_time(self, flight, date, time):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`, `flight_timings`.`id`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) AND strftime('%H', `time`) >= ? 
                    AND `flights`.`flight_no` = ? ORDER BY `date`, `time`'''
        if ( self._exec(query, [date, time, flight]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flight timing id '''
    def get_flight_timing_id(self, flight_no, date, time):
        query = ''' SELECT `id` FROM `flight_timings` WHERE
                    `flight_no`=? AND `date`=? AND `time`=? '''
        if ( self._exec(query, [flight_no, date, time]) ):
            return self.cursor.fetchone()
        return -1


    ''' Get all created flights '''
    def get_created_flights(self):
        query = ''' SELECT DISTINCT `flight_no` FROM `flights`'''
        if ( self._exec(query) ):
            return self.cursor.fetchall()
        return -1

    ''' Creates a new flight '''
    def create_flight(self, flight_no, airline, source, destination):
        query = '''INSERT INTO `flights` (`flight_no`, `airline`, `source`, `destination`)
        VALUES (?, ?, ?, ?)'''
        return self._exec(query, [flight_no, airline, source, destination])
        

    ''' Creates a new flight timing '''
    def create_flight_timing(self, flight_no, date, time):
        query = '''INSERT INTO `flight_timings` (`flight_no`, `date`, `time`) VALUES
                    (?, ?, ?)'''
        if self._exec(query, [flight_no, date, time]):
            return self.cursor.lastrowid
        return 0
    

    ''' Add flight seat counts '''
    def add_flight_seat_count(self, flight_no, first_class_seat, business_class_seat, economy_class_seat):
        query = '''INSERT INTO `flight_seat_map` (`flight_no`, `first_class_seat`, `business_class_seat`, `economy_class_seat`)
                    VALUES (?, ?, ?, ?)'''
        return self._exec(query, [flight_no, first_class_seat, business_class_seat, economy_class_seat])

        
    ''' Add flight price ampping '''
    def add_flight_price(self, flight_timing_id, first_class_price, business_class_price, economy_class_price):
        query = '''INSERT INTO `flight_price_map` (`flight_timing_id`, `first_class_price`, `business_class_price`, 
                    `economy_class_price`) VALUES (?, ?, ?, ?)'''
        return self._exec(query, [flight_timing_id, first_class_price, business_class_price, economy_class_price])
    

    ''' Delete existing flight '''
    def delete_flight(self, flights):
        query = "DELETE FROM `flights` WHERE "
        for i in flights:
            query += "`flight_no`=? OR "
        query = query[:-3]
        return self._exec(query, flights)
    

    ''' Delete all flight timings of particular flight '''
    def delete_flight_timing_from_flight(self, flight_no):
        query = "DELETE FROM `flight_timings` WHERE `flight_no`=?"
        return self._exec(query, [flight_no])
    

    ''' Delete all flight timings at given date'''
    def delete_flight_timing_from_date(self, date):
        query = "DELETE FROM `flight_timings` WHERE `date`=?"
        return self._exec(query, [date])
    

    ''' Delete all flight timings of particular flight at given date '''
    def delete_flight_timing_from_flight_date(self, flight_no, date):
        query = '''DELETE FROM `flight_timings` WHERE
                `flight_no`=? AND `date`=?'''
        return self._exec(query, [flight_no, date])


    ''' Delete all flight timings of particular flight at given date on given time'''
    def delete_flight_timing_from_flight_date_time(self, flight_no, date, time):
        query = '''DELETE FROM `flight_timings` WHERE 
                `flight_no`=? AND `date`=? AND `time`=?'''
        return self._exec(query, [flight_no, date, time])
    

    ''' Get seat count of given flight '''
    def get_seat_count(self, flight_no):
        query = ''' SELECT `first_class`, `business_class`, `economy_class` FROM 
                    `flight_seat_map` WHERE `flight_no`=? '''
        if ( self._exec(query, [flight_no]) ):
            return self.cursor.fetchall()
    

    ''' Get price of seats in a  given flight '''
    def get_flight_prices(self, flight_timing_id):
        query = ''' SELECT `first_class`, `business_class`, `economy_class` FROM 
                    `flight_price_map` WHERE `flight_timing_id`=? '''
        if ( self._exec(query, [flight_timing_id]) ):
            return self.cursor.fetchall()
        

    ''' Get complete details of a particular flight timing id '''
    def get_flight_details(self, flight_timing_id):
        query = ''' SELECT `flight_timings`.`flight_no`, `source`, `destination`, `airline`, `date`, `time`,
          `first_class_price`, `business_class_price`, `economy_class_price`, `first_class_seat`, 
          `business_class_seat`, `economy_class_seat` FROM `flight_timings`
            INNER JOIN `flights` ON `flight_timings`.`flight_no`=`flights`.`flight_no` 
            INNER JOIN `flight_seat_map` ON `flights`.`flight_no`=`flight_seat_map`.`flight_no`
            INNER JOIN `flight_price_map` ON `flight_price_map`.`flight_timing_id`=`flight_timings`.`id` 
            WHERE `flight_timings`.`id`=? '''
        if ( self._exec(query, [flight_timing_id]) ):
            return self.cursor.fetchall()
        
    
    def __del__(self):
        return super().__del__()