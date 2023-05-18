import os
import hashlib
import datetime
from services.db import DB

''' Creates session ID by getting random values and current timestamp and passing them to SHA256 '''
def generate_session_key():
    return hashlib.sha256(
        ( os.urandom(32).hex() +
        str(datetime.datetime.now().timestamp()) ).encode()
    )

''' Creates expires at value with interval of one day '''
def get_expires_at():
    return str(format(datetime.datetime.now() + datetime.timedelta(days=1), '%Y-%m-%d %H:%M:%S') )

''' Insert the session information into table '''
def create_admin_session(user_id):
    db = DB()
    db.delete_session(user_id)
    db.create_session(user_id, generate_session_key().hexdigest(), get_expires_at())