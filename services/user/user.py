import datetime
from services import session
from services.user.db import UserDB
from services.flight.db import FlightDB
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
    return db.delete_session(session_id)


''' Validates the user session '''
def validate_session(session_id):
    db = UserDB()
    expires_at = db.get_user_id_expires(session_id)
    if ( expires_at and datetime.datetime.strptime(expires_at[1], '%Y-%m-%d %H:%M:%S') > datetime.datetime.now() ):
        return True
    return False


''' Get available flights data based on date and time '''
def get_flights_data(date, time):
    fields = ["flight_no", "airline", "source", "destination",
              "date", "time"]
    db = FlightDB()
    if ( date and time ):
        res = db.get_flights_date_time(date, time[:2])
    elif ( date ):
        res = db.get_flights_date(date)
    else:
        res = db.get_all_flights()
    if res:
        return [ dict(zip(fields, list(x))) for x in res ]
    return 3
