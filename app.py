from flask import Flask
from src.endpoints.rocket_chat import rocket_chat

app = Flask(__name__)
app.register_blueprint(rocket_chat, url_prefix='/rocketchat')

@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/test', methods=['GET'])
# def test_rocketchat():
#     return "Hello World from test"

if __name__ == '__main__':
    app.run()


