import json

from flask import Flask
from requests import HTTPError

from src import configuration
from src.services import wikipedia

app = Flask(__name__)


def binary_to_dict(the_binary):
    jsn = ''.join(chr(int(x, 2)) for x in the_binary.split())
    d = json.loads(jsn)
    return d

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/wiki/<query>')
def wiki(query):
    try:
        return wikipedia(query)
    except HTTPError as e:
        return "Error during completion"


if __name__ == '__main__':
    configuration.load("configuration.dev.yaml")
    app.run()


