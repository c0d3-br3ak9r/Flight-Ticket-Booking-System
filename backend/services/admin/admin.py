import datetime
from services import session
import bcrypt
from services.admin.admin_db import AdminDB
from services.booking.booking_db import BookingDB


''' Adds admin user to database '''
def create_admin(username, password):
    db = AdminDB()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    if ( db.create_admin(username, hashed_pw.decode()) ):
        return 1
    return 3


''' Returns true if the admin credentials are valid '''
def login_admin(username, password):
    db = AdminDB()
    lst = db.get_admin_password(username)
    if ( not lst ):
        return 2
    user_id = lst[0]
    hashed_pw = lst[1]
    if ( hashed_pw and bcrypt.checkpw(bytes(password, 'utf-8'), bytes(hashed_pw, 'utf-8')) ):
        sid = session.create_admin_session(user_id)
        if ( sid ):
            return {"session_id" : sid}
        return 3
    return 2


''' Validates the admin session '''
def validate_session(session_id):
    db = AdminDB()
    expires_at = db.session_exists(session_id)
    if ( expires_at ):
        if ( datetime.datetime.strptime(expires_at[0], '%Y-%m-%d %H:%M:%S') > datetime.datetime.now() ):
            return True
        db.delete_session(session_id)
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
        res = db.get_all_bookings_from_date(date)
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