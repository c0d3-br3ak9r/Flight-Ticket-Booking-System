from services import validation
from services.admin import admin
from services.user import user
from services.flight import flight
from services.booking import booking


''' To create a new user '''
def create_user(payload):

    username = payload.get("username")
    password = payload.get("password")

    if ( validation.is_valid_username(username) and validation.is_valid_password(password) ):
        return user.create_user(username, password)
    return 2


''' To get flight details '''
def get_flights(session_id, payload):
    if ( session_id and user.validate_session(session_id) ):

        date = payload.get('date')
        time = payload.get('time')
        flight = payload.get('flight_no')

        flight = flight if flight and str.isalnum(flight) else None
        date = date if validation.is_valid_date(date) else None
        time = time if validation.is_valid_time(time) else None

        resp = user.get_flights_data(flight, date, time)
        if ( resp == 3 ):
            return 3
        return {
            "count" : len(resp),
            "flights" : resp
        }
    return 4


''' To book flight ticket '''
def book_flight(session_id, payload):
    if ( session_id and user.validate_session(session_id) ):

        flight = payload.get("flight_no")
        date = payload.get("date")
        time = payload.get("time")
        seat_no = payload.get("seat_no")
        if ( str.isalnum(flight) and validation.is_valid_date(date)
            and validation.is_valid_time(time) 
            and ( not seat_no or ( 1 <= seat_no <= 60 ) ) ):
                
                return booking.book_flight(session_id, flight, date, time, seat_no)
        return 2
    return 4


''' To get all bookings made by the user '''
def get_bookings(session_id):
    if ( session_id and user.validate_session(session_id) ):

        resp = booking.get_bookings(session_id)
        if ( resp == 3 ):
            return 3
        return {
            "count" : len(resp),
            "flights" : resp
        }
    return 4


''' To authenticate user '''
def authenticate_user(payload):

    username = payload.get("username")
    password = payload.get("password")    

    if ( validation.is_valid_username(username) and validation.is_valid_password(password) ):
        return user.login_user(username, password)
    return 2


''' To logout user '''
def logout_user(session_id):
    if ( session_id and user.validate_session(session_id) ):
        return user.logout_user(session_id)
    return 4


''' To create a new admin user '''
def create_admin(payload):

    username = payload.get("username")
    password = payload.get("password")

    if ( validation.is_valid_username(username) and validation.is_valid_password(password) ):
        return admin.create_admin(username, password)
    return 2


''' To authenticate admin '''
def authenticate_admin(payload):

    username = payload.get("username")
    password = payload.get("password")   

    if ( validation.is_valid_username(username) and validation.is_valid_password(password) ):
        return admin.login_admin(username, password)
    return 2


''' To create a flight '''
def create_flight(session_id, payload):

    flight_no = payload.get("flight_no")
    airline = payload.get("airline")
    source = payload.get("source")
    destination = payload.get("destination")

    if ( session_id and admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) and validation.strings_and_spaces(airline) and
            validation.strings_and_spaces(source) and validation.strings_and_spaces(destination) ):
                
                return flight.create_flight(flight_no, airline, source, destination)
    return 4


''' To create a flight timing '''
def create_flight_timing(session_id, payload):

    flight_no = payload.get("flight_no")
    time = payload.get("time")
    date = payload.get("date")

    if ( session_id and admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) and validation.is_valid_date(date) and
            validation.is_valid_time(time) ):

                return flight.create_flight_timing(flight_no, date, time)
        return 2
    return 4


''' To remove a flight '''
def remove_flight(session_id, payload):
    flight_no = payload.get("flight_no")

    if ( session_id and admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) ):
            return flight.remove_flight(flight_no)
        return 2
    return 4


''' To remove a flight timing '''
def remove_flight_timing(session_id, payload):

    flight_no = payload.get("flight_no")
    time = payload.get("time")
    date = payload.get("date")

    if ( session_id and admin.validate_session(session_id) ):
        if ( ( flight_no and str.isalnum(flight_no) ) or 
                ( date and validation.is_valid_date(date) ) or 
                ( time and validation.is_valid_time(time) ) ):
            return flight.remove_flight_timing(flight_no, date, time)
    return 4


''' To get all bookings '''
def get_all_bookings(session_id, payload):
    if ( session_id and admin.validate_session(session_id) ):

        flight = payload.get("flight_no")
        date = payload.get("date")
        time = payload.get("time")

        flight = flight if str.isalnum(flight) else None
        date = date if validation.is_valid_date(date) else None
        time = time if validation.is_valid_time(time) else None

        resp = admin.get_bookings(flight, date, time)
        if ( resp == 3 ):
            return 3
        return {
            "count" : len(resp),
            "flights" : resp
        }
    return 4


''' To logout admin '''
def logout_admin(session_id):
    if ( session_id and admin.validate_session(session_id) ):
        return admin.logout_admin(session_id)
    return 4