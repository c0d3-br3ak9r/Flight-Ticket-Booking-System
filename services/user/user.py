import datetime
from services import session
from services.user.user_db import UserDB
from services.flight.flight_db import FlightDB
import bcrypt


''' Adds user to database '''
def create_user(username, password):
    db = UserDB()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    if ( db.create_user(username, hashed_pw.decode()) ):
        return 1
    return 3


''' Authenticates user and creates session '''
def login_user(username, password):
    db = UserDB()
    lst = db.get_user_password(username)
    if ( not lst ):
        return 2
    user_id = lst[0]
    hashed_pw = lst[1]
    if ( hashed_pw and bcrypt.checkpw(bytes(password, 'utf-8'), bytes(hashed_pw, 'utf-8')) ):
        if ( session.create_user_session(user_id) ):
            return 1
        return 3
    return 2


''' Logout the user '''
def logout_user(session_id):
    db = UserDB()
    if ( db.delete_session(session_id) ):
        return 1
    return 3


''' Validates the user session '''
def validate_session(session_id):
    db = UserDB()
    expires_at = db.get_user_id_expires(session_id)
    if ( expires_at and datetime.datetime.strptime(expires_at[1], '%Y-%m-%d %H:%M:%S') > datetime.datetime.now() ):
        return True
    return False


''' Get available flights data based on date and time '''
def get_flights_data(flight_no, date, time):
    fields = ["flight_no", "airline", "source", "destination",
              "date", "time"]
    db = FlightDB()
    if ( flight_no and date and time ):
        res = db.get_flights_from_flight_date_time(flight_no, date, time)
    elif ( flight_no and date ):
        res = db.get_flights_from_flight_date(flight_no, date)
    elif ( date and time ):
        res = db.get_flights_from_date_time(date, time)
    elif ( date ):
        res = db.get_flights_from_date(date)
    elif ( flight_no ):
        res = db.get_flights_from_flight(flight_no)
    else:
        res = db.get_all_bookings()
    if ( res != -1 ):
        return [ dict(zip(fields, list(x))) for x in res ]
    return 3