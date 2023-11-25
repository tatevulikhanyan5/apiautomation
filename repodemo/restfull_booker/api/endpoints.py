class Endpoints:

    base_url = "https://reqres.in/api/"


    def get_user(self, user_id):
        get_user_url = self.base_url + f"user/{user_id}"
        return get_user_url

    def create_user(self):
        create_user_url = self.base_url + "users"
        return create_user_url

    def get_token_url(self):
        get_token = self.base_url + "register"
        return get_token




