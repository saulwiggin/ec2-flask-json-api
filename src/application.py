#!flask/bin/python
from flask import Flask
from flaskrun import flaskrun
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/', methods=['GET'])
def get():
    return '{"Output":"Hello World"}'

@application.route('/', methods=['POST'])
def post():
    return '{"Output":"Hello World"}'

if __name__ == '__main__':
    flaskrun(application)
