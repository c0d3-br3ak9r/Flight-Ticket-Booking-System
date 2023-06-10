import re
from datetime import datetime, date


''' Validates standard email in the format name@domain.com '''
def is_valid_email(email):
    return re.search("[a-zA-Z0-9.-]{4,20}@[a-zA-Z]{4,10}\.[a-z]{2,4}", email)


''' Validates username with lowercase, uppercase alphabets, digits and underscore
    with length between 4 and 20 '''
def is_valid_username(username):
    return re.search("^[a-zA-Z0-9_]{4,20}$", username)


''' Validates Password with atleast one uppercase letter, one lowercase letter, one digit,
 one special character (!@#$%^&+=.\-_*) between 8 and 16 characters long '''
def is_valid_password(password):
    return re.search("^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&+=.\-_*])([^\s]){8,16}$", password)


''' Validate if a string has only alphabets and spaces '''
def strings_and_spaces(s):
    return re.search("^[A-Za-z ]+$", s)


''' Validates if given date is in valid format and 
    is between current date and one year from now '''
def is_valid_date(date_val):
        try:
            dt = datetime.strptime(date_val, "%Y-%m-%d")
            curr = datetime.now()
            if ( date(curr.year, curr.month, curr.day) < dt.date() < date(curr.year+1, curr.month, curr.day) ):
                return True
            return False
        except ValueError:
            return False


''' Validates if given time is in valid format '''
def is_valid_time(date_text):
        try:
            datetime.strptime(date_text, "%H:%M:%S")
            return True
        except ValueError:
            return False