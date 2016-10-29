import json

from flask import Flask
from requests import HTTPError

from src import configuration
from src.services import wikipedia

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    configuration.load("configuration.dev.yaml")
    app.run()


