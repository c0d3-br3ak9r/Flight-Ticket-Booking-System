from services.flight.db import FlightDB


''' Add a new flight '''
def create_flight(flight_no, airline, source, destination):
    db = FlightDB()
    if ( db.create_flight(flight_no, airline, source, destination) ):
        return 1
    return 3


''' Create a flight timing for already created flight '''
def create_flight_timing(flight_no, date, timing):
    db = FlightDB()
    if ( db.create_flight_timing(flight_no, date, timing) ):
        return 1
    return 3


''' Delete a flight '''
def remove_flight(flight_no):
    db = FlightDB()
    if ( db.delete_flight(flight_no) ):
        return 1
    return 3


''' Delete timing slot of flight '''
def remove_flight_timing(flight_no, date, time):
    db = FlightDB()
    if ( flight_no and date and time ):
        res = db.delete_flight_timing_from_flight_date_time(flight_no, date, time)
    elif ( flight_no and date ):
        res = db.delete_flight_timing_from_flight_date(flight_no, date)
    elif ( flight_no ):
        res = db.delete_flight_timing_from_flight(flight_no)
    elif ( date ):
        res = db.delete_flight_timing_from_date(date)
    if ( res ):
        return 1
    return 3