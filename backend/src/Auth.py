import hashlib
import re
from src.DataStore import data_store
from src.Error import AccessError, InputError

class Account:
    def __init__(self, email, password, u_id):
        self.email = email
        self.password = generate_hash(password)
        self.id = u_id
        self.sessions = []

def generate_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

def auth_login(email, password):
    '''
    Given a registered user's email and password, returns their `u_id'
    value.

    Arguments:
        email (string)       - email address of a registered user
        password (string)    - password of a registered user

    Exceptions:
        InputError - Occurs when email entered does not belong to a user
        InputError - Occurs when password is not correct

    Return Value:
        Returns a dictionary containing the registered user's 
        'u_id' on successful match of user email and password
    '''
    return {
        'u_id': 0
    }

def auth_register(email, password):
    '''
    Given a user's email address, and password, create a new account for them and return a new `u_id`.

    Arguments:
        email (string)         - user's email address
        password (string)      - user's password

    Exceptions:
        InputError - Occurs when email entered is not a valid email
        InputError - Occurs when email address is already being used by another 
                     user
        InputError - Occurs when password is invalid

    Return Value:
        Returns a dictionary containing the registered user's 'u_id' on successful register of user
    '''

    return {
        'u_id': 0          
    } 

def auth_register_valid_email(email):
    '''
    Tests if an email passes a valid email format, returns True if it is valid
    and False if it is invalid.
    '''
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    if re.fullmatch(regex, email):
        return True
    return False