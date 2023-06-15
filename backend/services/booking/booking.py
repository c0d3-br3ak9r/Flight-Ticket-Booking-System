from services.booking.booking_db import BookingDB
from services.flight.flight_db import FlightDB
from services.user.user_db import UserDB
from services.flight import flight



''' Get user id from session '''
def get_user_id(session_id):
    udb = UserDB()
    user_id = udb.get_user_id_expires(session_id)
    print("user_id", user_id)
    if ( not user_id ):
        return 3
    return user_id[0]


''' Get booked Seats '''
def get_booked_seats(flight_no, date, time):
    bdb = BookingDB()
    booked_seats = bdb.get_booked_seats(flight_no, date, time)
    print("BOOked seats : ", booked_seats)
    if ( booked_seats == -1 ):
        return -1
    return [ x[0] for x in booked_seats ]


''' Book a flight ticket '''
def book_flight(session_id, flight_no, date, time, users):

    bdb = BookingDB()
    
    timing_id = flight.get_flight_timing_id(flight_no, date, time)
    user_id = get_user_id(session_id)

    price = 0

    fdb = FlightDB()
    prices = fdb.get_flight_prices(timing_id)
    if ( prices ):
        firstClassPrice, businessClassPrice, economyClassPrice = prices[0]

    for user in users:
        if ( user["seat_no"][0] == 'F' ):
            user["price"] = firstClassPrice
            price += firstClassPrice
        elif ( user["seat_no"][0] == 'B' ):
            user["price"] = businessClassPrice
            price += businessClassPrice
        elif ( user["seat_no"][0] == 'E' ):
            user["price"] = economyClassPrice
            price += economyClassPrice

    booking_id =  bdb.create_booking(user_id, timing_id, price)
    print(booking_id)
    if ( booking_id != 0 ):
        user_details = []
        for user in users:
            user["booking_id"] = booking_id
            user_details.append(list(user.values()))
        print(user_details)
        return bdb.insert_user_details(user_details)
    return 3



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
