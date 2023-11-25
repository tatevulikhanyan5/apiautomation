from repodemo.restfull_booker.tests.base_test import BaseTest


class TestPostRequests(BaseTest):

    def test_create_user(self):
        self.create_new_user()

    def test_get_token_and_create_user(self):
        self.create_user_via_auth()

