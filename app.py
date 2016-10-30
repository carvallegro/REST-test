import json

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test', methods=['GET'])
def test_rocketchat():
    return "Hello World from test"

if __name__ == '__main__':
    app.run()


