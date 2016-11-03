import os

from flask import Blueprint, jsonify, make_response

from discourse import access

access.configuration(_base_url=os.environ['DISCOURSE_BASE_URL'],
                     _api_key=os.environ['DISCOURSE_API_KEY'],
                     _username=os.environ['DISCOURSE_USERNAME'])

discourse_blueprint = Blueprint('rocketchat', __name__)


@discourse_blueprint.route('/test', methods=['GET'])
def test_rocketchat():
    return "Hello World from test"


@discourse_blueprint.route('/latest', methods=['GET'])
def latest_posts():
    latest_posts = access.latest()
    return jsonify(latest_posts)


@discourse_blueprint.route('/user/<username>/infos')
def user_infos(username):
    infos = access.user_info(username)
    response = make_response(infos.toJSON())
    response.headers['Content-Type'] = 'application/json';
    return response


@discourse_blueprint.errorhandler(500)
def generic_error_handler(error):
    return jsonify(error.__dict__)