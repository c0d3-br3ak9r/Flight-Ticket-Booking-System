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
        if date_val is None:
             return False
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
        if date_text is None:
             return False
        try:
            datetime.strptime(date_text, "%H:%M")
            return True
        except ValueError:
            return False
        

''' Validates user details '''
def validate_user(user, f, b, e):
    try:
        clss, no = user["seat_no"][0], int(user["seat_no"][1])
    except Exception as e:
        return False
    print(clss,no, f)
    print(strings_and_spaces(user["name"]), (1 <= user["age"] <= 200),
          (user["gender"] == "Male" or "Female" or "Others" ), ( clss == 'F' or 'B' or 'E'),
          (
        ( clss == 'F' and no >= 1 and no <= f ) or
        ( clss == 'B' and no >= 1 and no <= b ) or
        ( clss == 'E' and no >= 1 and no <= e )
        ))
    return (strings_and_spaces(user["name"]) and (1 <= user["age"] <= 200) and (
        user["gender"] == "Male" or "Female" or "Others" ) and ( clss == 'F' or 'B' or 'E') and (
        ( clss == 'F' and no >= 1 and no <= f ) or
        ( clss == 'B' and no >= 1 and no <= b ) or
        ( clss == 'E' and no >= 1 and no <= e )
        ))