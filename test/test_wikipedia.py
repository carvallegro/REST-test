from unittest import TestCase
from httmock import urlmatch, HTTMock, all_requests, response
import json

from src.services import get_wikipedia


@urlmatch(netloc=r'(.*\.)?wikipedia\.org(.*\.)')
def google_mock(url, request):
    return 'Feeling lucky, punk?'

@all_requests
def response_content(url, request):
    url_path = url.path.split('/')
    query = url_path[-1]
    print(url_path)
    code = 200
    if len(url_path) is not 6:
        code = 500

    headers = {'content-type': 'application/json', 'Set-Cookie': 'foo=bar;'}
    content = {'message': 'API rate limit exceeded'}
    return response(code, content, headers, None, 5, request)

class TestWikipedia(TestCase):

    def test_exemple_wikipedia(self):
        with HTTMock(response_content):
            result = get_wikipedia('test')
        assert result == {'message': 'API rate limit exceeded'}

    # Todo more tests !!