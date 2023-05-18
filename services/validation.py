import re

def is_valid_email(email):
    print("Email :", re.search("[a-zA-Z0-9.-]{4,20}@[a-zA-Z]{4,10}\.[a-z]{2,4}", email))
    return re.search("[a-zA-Z0-9.-]{4,20}@[a-zA-Z]{4,10}\.[a-z]{2,4}", email)

def is_valid_username(username):
    print("Username :", re.search("^[a-zA-Z0-9_]{4,20}$", username))
    return re.search("^[a-zA-Z0-9_]{4,20}$", username)

''' Validates Password with atleast one uppercase letter, one lowercase letter, one digit,
 one special character (!@#$%^&+=.\-_*) between 8 and 16 characters long '''
def is_valid_password(password):
    print("Password :", re.search("^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&+=.\-_*])([^\s]){8,16}$", password))
    return re.search("^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&+=.\-_*])([^\s]){8,16}$", password)