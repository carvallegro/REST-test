import requests


def wikipedia(query):
    http_response = get_wikipedia(query)
    return http_response['extract']


# made using http://www.programmableweb.com/api/wikipedia
def get_wikipedia(query):
    http_response = requests.get("https://fr.wikipedia.org/api/rest_v1/page/summary/" + query)
    if http_response.status_code is not requests.codes.ok:
        raise http_response.raise_for_status()
    return http_response.json()