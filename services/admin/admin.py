import datetime
from services import validation
import bcrypt
from services.admin.admin_db import AdminDB
from services.booking.booking_db import BookingDB

''' Returns true if the admin credentials are valid '''
def is_valid_user(username, password):
    if ( validation.is_valid_username(username) and 
        validation.is_valid_password(password) ):
        db = AdminDB()
        lst = db.get_admin_password(username)
        if ( not lst ):
            return 0
        user_id = lst[0]
        hashed_pw = lst[1]
        if ( hashed_pw and bcrypt.checkpw(bytes(password, 'utf-8'), bytes(hashed_pw, 'utf-8')) ):
            return user_id
    return 0

''' Validates the admin session '''
def validate_session(session_id):
    db = AdminDB()
    expires_at = db.session_exists(session_id)
    if ( expires_at and datetime.datetime.strptime(expires_at[0], '%Y-%m-%d %H:%M:%S') > datetime.datetime.now() ):
        return True
    return False


''' Get bookings based on flight, date and time '''
def get_bookings(flight_no, date, time):
    fields = ["booking_id", "username", "flight_no", "source", "destination",
              "airline", "date", "time", "seat_no"]
    db = BookingDB()
    if ( flight_no and date and time ):
        res = db.get_all_bookings_from_flight_date_time(flight_no, date, time)
    elif ( flight_no and date ):
        res = db.get_all_bookings_from_flight_date(flight_no, date)
    elif ( flight_no ):
        res = db.get_all_bookings_from_flight(flight_no)
    elif ( date ):
        res = db.get_all_bookings_from_flight_date(date)
    else:
        res = db.get_all_bookings()
    if ( res != -1 ):
        return [ dict(zip(fields, list(x))) for x in res ]
    return 3


''' Logout the admin '''
def logout_admin(session_id):
    db = AdminDB()
    if ( db.delete_session(session_id) ):
        return 1
    return 3