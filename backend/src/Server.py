from json import dumps
from flask import Flask, request
from flask_cors import CORS
from src import Config
from src.DataStore import data_store

from src.Auth import auth_login, auth_register
from src.Clear import clear

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)

@APP.route("/auth/login", methods=['POST'])
def app_auth_login():
    data = request.get_json()
    return auth_login(
        data['email'],
        data['password']
    )

@APP.route("/auth/register", methods=['POST'])
def app_auth_register():
    data = request.get_json()
    return auth_register(
        data['email'],
        data['password'],
    )

@APP.route("/clear", methods=['DELETE'])
def app_clear():
    return clear()

if __name__ == "__main__":
    APP.run(port=Config.port)  # Do not edit this port
