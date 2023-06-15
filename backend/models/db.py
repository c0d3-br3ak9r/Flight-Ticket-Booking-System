import sqlite3

class DB:
    
    enforce_foreign_key = "PRAGMA foreign_keys = ON;"


    def __init__(self):
        try:
            self.conn = sqlite3.connect("flight_ticket_booking_database.db")
            self.cursor = self.conn.cursor()
            self._exec(self.enforce_foreign_key)
        except sqlite3.Error as e:
            print("DB ERROR :", e)
            self.conn = None


    ''' Executes the SQL query '''
    def _exec(self, query, params=[]):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return 1
        except sqlite3.Error as e:
            print(e)
            return 0
        
    ''' Executes mulitple SQL query '''
    def _execmany(self, query, params=[]):
        try:
            self.cursor.executemany(query, params)
            self.conn.commit()
            return 1
        except sqlite3.Error as e:
            print(e)
            return 0


    def __del__(self):
        self.cursor.close()
        self.conn.close()
