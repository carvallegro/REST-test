from flask import Blueprint

rocket_chat = Blueprint('rocketchat', __name__)

@rocket_chat.route('/test', methods=['GET'])
def test_rocketchat():
    return "Hello World from test"