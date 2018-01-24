#!flask/bin/python
from flask import Flask
from flaskrun import flaskrun
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

# @application.route('/json', methods=['GET'])
# def get():
#     ref_chromo = Chromosome(1).sequence(21786068,21786118)
#     return '{"Vitamin B6":"'+ref_chromo+'"}'

@application.route('/', methods=['GET'])
def get():
    return '{"Output":"Hello World"}'

@application.route('/', methods=['POST'])
def post():
    return '{"Output":"Hello World"}'

if __name__ == '__main__':
    flaskrun(application)
