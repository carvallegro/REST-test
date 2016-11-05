import os

from flask import Blueprint, jsonify, make_response

from src.discourse import access

access.configuration(_base_url=os.environ['DISCOURSE_BASE_URL'],
                     _api_key=os.environ['DISCOURSE_API_KEY'],
                     _username=os.environ['DISCOURSE_USERNAME'])

discourse_blueprint = Blueprint('disourse', __name__)


@discourse_blueprint.route('/', methods=['GET'])
def hello_world():
    return "Hello World from /discourse"


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
