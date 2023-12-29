import pytest
import requests
from src.Error import InputError
from src import Config

@pytest.fixture
def clear_data():
    requests.delete(f'{Config.url}clear')

def test_register_invalid_email_missing_at_symbol(clear_data):
    '''
    InputError when: email entered is missing '@'
    '''
    response = requests.post(f'{Config.url}auth/register', json={
        'email': 'email.com', 
        'password': 'password', 
    })
    assert response.status_code == InputError.code

def test_register_invalid_email_missing_fullstop(clear_data):
    '''
    InputError when: email entered is missing '.'
    '''
    response = requests.post(f'{Config.url}auth/register', json={
        'email': 'email@outlook', 
        'password': 'password', 
    })
    assert response.status_code == InputError.code

def test_register_email_taken(clear_data):
    '''
    InputError when: email address is already being used by another user
    '''
    requests.post(f'{Config.url}auth/register', json={
        'email': 'me@outlook.com', 
        'password': 'password', 
    })

    response = requests.post(f'{Config.url}auth/register', json={
        'email': 'me@outlook.com', 
        'password': 'password', 
    })
    assert response.status_code == InputError.code

def test_register_password_invalid(clear_data):
    '''
    InputError when: length of password is less than 6 characters
    '''
    response = requests.post(f'{Config.url}auth/register', json={
        'email': 'me@outlook.com', 
        'password': '12345', 
    })
    assert response.status_code == InputError.code

def test_register_id_matches_login_id_one_user(clear_data):
    '''
    Tests if the 'u_id' returned by auth_register and auth_login match 
    when registering in a single user
    '''
    response_register = requests.post(f'{Config.url}auth/register', json={
        'email': 'me@outlook.com', 
        'password': 'password', 
    })
    register_id = response_register.json()['u_id']
    
    response_login = requests.post(f'{Config.url}auth/login', json={
        'email': 'me@outlook.com', 
        'password': 'password', 
    })
    
    login_id = response_login.json()['u_id']

    assert register_id == login_id

