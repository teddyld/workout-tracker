import requests
from src import Config
from src.Constants import OK_CODE
from src.Error import InputError

def test_clear_response_and_return():
    response = requests.delete(f'{Config.url}/clear')
    assert response.status_code == OK_CODE
    response_data = response.json()
    assert response_data == {}

def test_clear_register_user():
    '''
    Test if the registered user is cleared in the data_store after clear is 
    called
    '''
    requests.delete(f'{Config.url}/clear')

    requests.post(f'{Config.url}/auth/register', json={
        'email': 'email@outlook.com',
        'password': 'password',
    })

    requests.delete(f'{Config.url}/clear')
    
    response = requests.post(f'{Config.url}/auth/login', json={
        'email': 'email@outlook.com',
        'password': 'password',
    })
    assert response.status_code == InputError.code