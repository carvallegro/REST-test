from unittest import TestCase
import json

from . import user_output, user_input, badge_input, badge_output

from src.discourse.models import user

class TestUser(TestCase):

    def test_should_do_default_init_behavior_for_user_vcarmignac(self):
        self.compare_user_json_input_output('vcarmignac')

    def test_user_sherlock_should_have_system_avatar(self):
        self.compare_user_json_input_output('sholmes')

    def compare_user_json_input_output(self, username):
        imported_user = user.User(user_input(username))
        self.assertEqual(json.loads(imported_user.toJSON()), user_output(username))


    def test_member_badge_should_be_correctly_imported(self):
        self.compare_badge_json_input_output('member')

    def compare_badge_json_input_output(self, badge):
        imported_badge = user.Badge(badge_input(badge))
        self.assertEqual(json.loads(imported_badge.toJSON()), badge_output(badge))

