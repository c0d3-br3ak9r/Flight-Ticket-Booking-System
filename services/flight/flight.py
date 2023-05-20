import datetime
from services import validation
from services.flight.db import FlightDB


def create_flight(flight_no, airline, source, destination):
    if ( str.isalnum(flight_no) and validation.strings_and_spaces(airline) and
            validation.strings_and_spaces(source) and validation.strings_and_spaces(destination) ):
        db = FlightDB()
        if ( db.create_flight(flight_no, airline, source, destination) ):
            return ("Success", 201)
        return ("Database erorr", 500)
    return ('Bad Request', 400)


def create_flight_timing(flight_no, date, timing):
    if ( str.isalnum(flight_no) and validation.is_valid_date(date) and
            validation.is_valid_time(timing) ):
        db = FlightDB()
        if ( db.create_flight_timing(flight_no, date, timing) ):
            return ("Success", 201)
        return ("Database erorr", 500)
    return ('Bad Request', 400)


def remove_flight(flight_no):
    db = FlightDB()
    if ( db.delete_flight(flight_no) ):
        return 1
    return 3