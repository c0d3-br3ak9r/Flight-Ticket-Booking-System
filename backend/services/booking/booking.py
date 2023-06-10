from services.booking.booking_db import BookingDB
from services.flight.flight_db import FlightDB
from services.user.user_db import UserDB


''' Book a flight ticket '''
def book_flight(session_id, flight_no, date, time, seat_no):

    bdb = BookingDB()
    fdb = FlightDB()
    udb = UserDB()

    booked_seats = bdb.get_booked_seats(flight_no, date, time)
    if ( booked_seats == -1 ):
        return 3
    booked_seats = [] if not booked_seats else [x[0] for x in booked_seats]
    
    # If seat no is not given, pick first available seat
    if ( not seat_no ):               
        for i in range(1, 61):
            if ( i not in booked_seats ):
                seat_no = i
                break

    if ( seat_no not in booked_seats ):
        timing_id = fdb.get_flight_timing_id(flight_no, date, time)
        del fdb
        if ( timing_id == -1 ):
            return 3
        timing_id = timing_id[0]
        
        user_id = udb.get_user_id_expires(session_id)
        del udb
        if ( not user_id ):
            return 3
        user_id = user_id[0]
        
        return bdb.create_booking(user_id, timing_id, seat_no)
    return 2


''' Get user id from session id and get all bookings '''
def get_bookings(session_id):
    udb = UserDB()
    user_id = udb.get_user_id_expires(session_id)
    del udb

    if ( not user_id ):
        return 3
    user_id = user_id[0]
    
    bdb = BookingDB()
    res = bdb.get_all_bookings_from_user(user_id)
    fields = ["booking_id", "username", "flight_no", "source", "destination",
              "airline", "date", "time", "seat_no"]
    if ( res != -1 ) :
        return [ dict(zip(fields, list(x))) for x in res ]
    return 3
