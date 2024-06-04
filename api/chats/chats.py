import os
import requests
from dotenv import load_dotenv

load_dotenv()


class ChatAPI:

    def chat_list(self):
        url = os.getenv('CHAT_LIST')
        respond = requests.get(url)
        return respond.json()
