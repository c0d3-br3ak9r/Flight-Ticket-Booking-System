from services.booking.booking_db import BookingDB
from services.flight.db import FlightDB
from services.user.db import UserDB

''' Book a flight ticket '''
def book_flight(session_id, flight_no, date, time, seat_no):
    bdb = BookingDB()
    fdb = FlightDB()
    udb = UserDB()
    booked_seats = bdb.get_booked_seats(flight_no, date, time)
    print("booked_sets :", booked_seats)
    booked_seats = [] if booked_seats == None else list(booked_seats)
    if ( booked_seats == -1 ):
        return 3
    
    # If seat no is not given, pick first available seat
    if ( not seat_no ):                     
        for i in range(1, 61):
            if ( i not in booked_seats ):
                seat_no = i
                break

    if ( seat_no not in booked_seats ):
        timing_id = fdb.get_flight_timing_id(flight_no, date, time)[0]
        del fdb
        print("Timing ID :", timing_id)
        if ( not timing_id ):
            return 3
        user_id = udb.get_user_id_expires(session_id)[0]
        del udb
        print("User ID :", user_id)
        if ( not user_id ):
            return 3
        return bdb.create_booking(user_id, timing_id, seat_no)
    return 2


''' Get user id from session id and get all bookings '''
def get_bookings(session_id):
    udb = UserDB()
    user_id = udb.get_user_id_expires(session_id)[0]
    del udb
    if ( not user_id ):
        return 3
    bdb = BookingDB()
    res = bdb.get_all_bookings_from_user(user_id)
    fields = ["booking_id", "username", "flight_no", "source", "destination",
              "airline", "date", "time", "seat_no"]
    if res:
        return [ dict(zip(fields, list(x))) for x in res ]
    return 3
