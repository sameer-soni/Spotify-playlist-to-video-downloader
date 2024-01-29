import json

from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

Client_id = os.getenv("CLIENT_ID")
Client_secret = os.getenv("CLIENT_SECRET")
# print(Client_id,Client_secret)


def get_token():
    auth_string = Client_id + ':' + Client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str((base64.b64encode(auth_bytes).decode("utf-8")))

    url = "https://accounts.spotify.com/api/token"
    headers = {
        'Authorization': "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": 'client_credentials'}

    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}