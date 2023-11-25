import pytest

from repodemo.restfull_booker.api.rest_requests import Rest

@pytest.mark.usefixtures('get_driver')
class BaseTest(Rest):

    def get_user_by_id(self, user_id):
        url = self.endpoints.get_user(user_id)
        response = self.make_get_request(url)
        assert response["data"]["id"]==user_id

    def create_new_user(self):
        url = self.endpoints.create_user()
        body = self.jsons.create_user_json()
        response = self.make_post_request(url, json_body=body)
        assert response["name"]=="Tat"

    def get_token(self):
        url = self.endpoints.get_token_url()
        body = self.jsons.generate_token_json()
        response = self.make_post_request(url, json_body=body, status_code=200)
        return response

    def create_user_via_auth(self):
        url = self.endpoints.create_user()
        body = self.jsons.create_user_json()
        login = self.get_token()
        token = login["token"]
        self.make_post_request_with_auth(url, json_body=body, bearer=token, status_code=201)
