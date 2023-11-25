class JsonBuilders:

    def create_user_json(self):
        create_user_dict = {
            "name": "Tat",
            "job": "Ulyan",
            "id": "723",
            "createdAt": "2023-11-23T21:44:59.385Z"
        }
        return create_user_dict

    def generate_token_json(self):
        token_dict = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        return token_dict