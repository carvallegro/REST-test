import json
import os
from unittest import TestCase, main

from httmock import HTTMock, urlmatch

from src.discourse import access
from src.discourse.models.user import NoUserError

DIR_PATH = os.path.dirname(os.path.abspath(__file__));
MOCK_DISCOURSE_REGEX = r'(.*\.)?discourse\.mock\.com$'


class TestConfiguration(TestCase):
    def setUp(self):
        # self.maxDiff = None
        access.configuration('https://www.discourse.mock.com', 'username', 'token_api')

    def test_should_return_proper_user_for_vcarmignac(self):
        self.compare_userinfo_input_and_output('vcarmignac')

    def test_should_return_404_error(self):
        # Arrange
        expected = NoUserError('nouser')

        # Act & Assert
        with self.assertRaises(NoUserError) as context:
            with HTTMock(user_info_mock):
                access.user_info('nouser')

        self.assertEqual(context.exception.toJSON(), '{"message": "nouser does\'n exist on Discouse"}')

    def compare_userinfo_input_and_output(self, username):
        # Arrange
        expected = user_info_output(username)

        # Act
        with HTTMock(user_info_mock):
            result = access.user_info(username)

        # Assert
        self.assertEqual(json.loads(result.toJSON()), expected)


@urlmatch(netloc=MOCK_DISCOURSE_REGEX, path=r'\/users\/[a-z]*\.json', method='GET')
def user_info_mock(url, request):
    username = url.path.replace('/users/', '').replace('.json', '')
    try:
        with open(DIR_PATH + '/input/userinfo_{user}.json'.format(user=username), 'r') as f:
            result = f.read();
    except IOError:
        return {'status_code': 404, 'content': 'not found'}
        # http_error = HTTPError()
        # http_error.response = {'status_code': 404}
        # raise http_error

    return {'status_code': 200,
            'content': result}


def user_info_output(username):
    with open(DIR_PATH + '/output/userinfo_{}.json'.format(username)) as data_file:
        expected = json.load(data_file)
    return expected


if __name__ == '__main__':
    main()
