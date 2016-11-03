import json
import os
from unittest import TestCase, main

from httmock import HTTMock, urlmatch

from src.discourse import access

dirpath = os.path.dirname(os.path.abspath(__file__));

# define matcher:
# @all_requests
@urlmatch(netloc=r'(.*\.)?discourse_test\.mock\.com$')
def basic_mock(url, request):
    with open(dirpath+'/input/userinfo_vcarmignac.json', 'r') as f:
        result = f.read();
    return {'status_code': 200,
            'content': result}


def user_info(username):
    with HTTMock(basic_mock):
        result = access.user_info(username)
    return result


def user_info_output(username):
    with open(dirpath+'/output/userinfo_{}.json'.format(username)) as data_file:
        expected = json.load(data_file)
    return expected


class TestConfiguration(TestCase):
    def setUp(self):
        access.configuration('https://www.discourse_test.mock.com', 'username', 'token_api')

    def test_should_return_proper_user_for_vcarmignac(self):
        self.compare_userinfo_input_and_output('vcarmignac')

    def compare_userinfo_input_and_output(self, username):
        self.maxDiff = None

        result = user_info(username)

        expected = user_info_output(username)

        self.assertEqual(json.loads(result.toJSON()), expected)


if __name__ == '__main__':
    main()
