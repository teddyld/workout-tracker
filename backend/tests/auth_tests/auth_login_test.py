import pytest
import requests
from src.Error import InputError
from src import Config

@pytest.fixture
def clear_data_and_register_user():
    requests.delete(f'{Config.url}clear')
    requests.post(f'{Config.url}auth/register', json={
        'email': 'me@outlook.com', 
        'password': 'password', 
    })

def test_login_invalid_email(clear_data_and_register_user):
    '''
    InputError when: entered email does not belong to an existing user
    '''
    response = requests.post(f'{Config.url}auth/login', json={
        'email': 'notme@outlook.com', 
        'password': 'password', 
    })
    assert response.status_code == InputError.code

def test_login_invalid_password(clear_data_and_register_user):
    '''
    InputError when: login password is incorrect
    '''
    response = requests.post(f'{Config.url}auth/login', json={
        'email': 'me@outlook.com', 
        'password': 'not_the_password', 
    })
    assert response.status_code == InputError.code
