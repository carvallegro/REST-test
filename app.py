import json

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test_rocketchat():
    return '{' \
           '"text":"HOLa fdfs"' \
           '}'

if __name__ == '__main__':
    app.run()


