import os
import requests
from dotenv import load_dotenv

load_dotenv()


class UserAPI:

    def add_user(self, data):
        url = os.getenv('ADD_USER')
        respond = requests.post(url, data=data)

        if respond.status_code == 201:
            return respond.json()

