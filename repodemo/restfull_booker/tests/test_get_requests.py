from repodemo.restfull_booker.tests.base_test import BaseTest


class TestGetRequests(BaseTest):

    def test_get_user(self):
        self.get_user_by_id(2)