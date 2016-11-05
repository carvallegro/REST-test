import os
import json

DIR_PATH = os.path.dirname(os.path.abspath(__file__));


def badge_output(badge):
    return get_json_file('output', 'badge_' + badge)


def badge_input(badge):
    return get_json_file('input', 'badge_' + badge)

def user_output(username):
    return get_json_file('output', 'user_' + username)


def user_input(username):
    return get_json_file('input', 'user_' + username)


def get_json_file(folder, filename):
    with open('{dir}/{folder}/{file}.json'.format(dir=DIR_PATH, folder=folder, file=filename)) as data_file:
        return json.load(data_file)
