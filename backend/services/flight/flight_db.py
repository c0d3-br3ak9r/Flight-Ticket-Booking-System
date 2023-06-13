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


    def __init__(self):
        super().__init__()
        self._exec(self.create_flight_table)
        self._exec(self.create_flight_timing_table)


    ''' Get all upcoming flights '''
    def get_all_flights(self):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) >= DATE('now')'''
        if ( self._exec(query) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on flight '''
    def get_flights_from_flight(self, flight):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE `flights`.`flight_no` = ?'''
        if ( self._exec(query, [flight]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date '''
    def get_flights_from_date(self, date):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) ORDER BY `date`, `time`'''
        if ( self._exec(query, [date]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date of particular flight '''
    def get_flights_from_flight_date(self, flight, date):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) AND `flights`.`flight_no` = ?'''
        if ( self._exec(query, [date, flight]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date and time '''
    def get_flights_from_date_time(self, date, time):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) AND strftime('%H', `time`) >= ? '''
        if ( self._exec(query, [date, time]) ):
            return self.cursor.fetchall()
        return -1
    

    ''' Get flights based on date and time of particular flight'''
    def get_flights_from_flight_date_time(self, flight, date, time):
        query = ''' SELECT `flights`.`flight_no`, `airline`, `source`, `destination`, `date`, `time`
                    FROM `flights` INNER JOIN `flight_timings`
                    ON `flights`.`flight_no` = `flight_timings`.`flight_no` 
                    WHERE DATE(`date`) = DATE(?) AND strftime('%H', `time`) >= ? 
                    AND `flights`.`flight_no` = ? '''
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
        return self._exec(query, [flight_no, date, time])
    

    ''' Delete existing flight '''
    def delete_flight(self, flight_no):
        query = "DELETE FROM `flights` WHERE `flight_no`=?"
        return self._exec(query, [flight_no])
    

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
    
    
    def __del__(self):
        return super().__del__()