from services.flight.flight_db import FlightDB
from services.booking import booking


''' Add a new flight '''
def create_flight(flight_no, airline, source, destination, first_class_count, business_class_count, economy_class_count):
    db = FlightDB()
    if ( db.create_flight(flight_no, airline, source, destination) ):
        if ( db.add_flight_seat_count(flight_no, first_class_count, business_class_count, economy_class_count) ):
            return 1
    return 3


''' Create a flight timing for already created flight '''
def create_flight_timing(flight_no, date, timing, first_class_price, business_class_price, economy_class_price):
    db = FlightDB()
    flight_timing_id =  db.create_flight_timing(flight_no, date, timing)
    if ( flight_timing_id ):
        if ( db.add_flight_price(flight_timing_id, first_class_price, business_class_price, economy_class_price) ):
            return 1
    return 3


''' Get created flights '''
def get_created_flights():
    db = FlightDB()
    res = db.get_created_flights()
    if ( res != -1 ):
        return {"count" : len(res), "flights": [ x[0] for x in res ] }
    return 3


''' Get flight timing id from flight details '''
def get_flight_timing_id(flight_no, date, time):
    fdb = FlightDB()
    timing_id = fdb.get_flight_timing_id(flight_no, date, time)
    if ( timing_id == -1 ):
        return 3
    return timing_id[0]


''' Get seat count '''
def get_seat_count(flight):
    fdb = FlightDB()
    seats = fdb.get_seat_count(flight)
    if ( len(seats[0]) != 3 ):
        return -1
    return seats[0]


''' Get complete flight details '''
def get_flight_details(flight_timing_id):
    fields = ["flight_no", "source", "destination", "airline", "date", "time", "first_class_price",
              "business_class_price", "economy_class_price", "first_class_seat", "business_class_seat",
              "ecconomy_class_seat", "booked_seats"]
    fdb = FlightDB()
    res = fdb.get_flight_details(flight_timing_id)
    if ( res ):
        tmp = dict(zip(fields, list(res[0])))
        booked_seats = booking.get_booked_seats(tmp["flight_no"], tmp["date"], tmp["time"])
        tmp["booked_seats"] = booked_seats
        return tmp


''' Delete a flight '''
def remove_flight(flights):
    db = FlightDB()
    if ( db.delete_flight(flights) ):
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