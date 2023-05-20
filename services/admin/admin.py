import datetime
from services import validation
import bcrypt
from services.admin.db import AdminDB

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