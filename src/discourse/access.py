import requests

from discourse.models.user import User

base_url = 'BASE_URL'
api_key = 'API_KEY'
username = 'USERNAME'


def configuration(_base_url, _api_key, _username):
    global base_url
    base_url = _base_url
    global api_key
    api_key = _api_key
    global username
    username = _username


def url(action):
    auth_suffix = '?api_key={0}&api_username={1}'.format(api_key, username)
    return base_url + action + auth_suffix


def get(action, cls=None, data={}):
    request_result = requests.get(url(action), data=data)
    if request_result.status_code is not requests.codes.ok:
        request_result.raise_for_status()

    json_result = request_result.json()
    if cls is None:
        return json_result
    return cls(json=json_result)


def latest():
    return get('/latest.json')

def user_info(username):
    return get('/users/{0}.json'.format(username), cls=User)
