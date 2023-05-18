from services import validation
import bcrypt
from services.db import DB

''' Returns true if the admin credentials are valid '''
def is_valid_user(username, password):
    if ( validation.is_valid_username(username) and 
        validation.is_valid_password(password) ):
        db = DB()
        hashed_pw = db.get_admin_password(username)
        if ( hashed_pw ):
            return bcrypt.checkpw(bytes(password, 'utf-8'), bytes(hashed_pw, 'utf-8'))
    return False