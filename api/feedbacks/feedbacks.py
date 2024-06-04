import os
import requests
from dotenv import load_dotenv

load_dotenv()


class FeedbackAPI:

    def add_feedback(self, data):
        url = os.getenv('ADD_FEEDBACK')
        respond = requests.post(url, data=data)

        if respond.status_code == 201:
            return respond.json()
