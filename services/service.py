from services import session, validation
from services.admin import admin
from services.user import user
from services.flight import flight


''' To create a new user '''
def create_user(payload):
    username = payload.get("username")
    password = payload.get("password")
    if ( validation.is_valid_username(username) and validation.is_valid_password(password) ):
        return user.create_user(username, password)
    return 2


''' To get flight details '''
def get_flights(session_id, payload):
    if ( user.validate_session(session_id) ):
        date = payload.get('date')
        time = payload.get('time')
        date = date if validation.is_valid_date(date) else None
        time = time if validation.is_valid_time(time) else None
        resp = user.get_flights_data(date, time)
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


''' To create a flight '''
def create_flight(session_id, flight_no, airline, source, destination):
    if ( admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) and validation.strings_and_spaces(airline) and
            validation.strings_and_spaces(source) and validation.strings_and_spaces(destination) ):
            return flight.create_flight(flight_no, airline, source, destination)
    return "Forbidden", 403


''' To create a flight timing '''
def create_flight_timing(session_id, flight_no, date, time):
    if ( admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) and validation.is_valid_date(date) and
            validation.is_valid_time(time) ):
            return flight.create_flight_timing(flight_no, date, time)
        return 2
    return 4


''' To remove a flight '''
def remove_flight(session_id, flight_no):
    if ( session_id and admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) ):
            return flight.remove_flight(flight_no)
        return 2
    return 4


''' To remove a flight timing '''
def remove_flight_timing(session_id, flight_no, date, time):
    if ( session_id and admin.validate_session(session_id) ):
        if ( ( flight_no and str.isalnum(flight_no) ) or 
                ( date and validation.is_valid_date(date) ) or 
                ( time and validation.is_valid_time(time) ) ):
            return flight.remove_flight_timing(flight_no, date, time)
    return 4