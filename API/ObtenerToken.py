import os
from dotenv import load_dotenv
import requests
import urllib3 # Evitar warnings de SSL

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
load_dotenv()

def obtener_token():
    url = os.getenv("API_TOKEN_URL")
    body = {"username": os.getenv("AUTH_USERNAME"), "password": os.getenv("AUTH_PASSWORD")}
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=body, headers=headers, verify=False)
    resp.raise_for_status()
    data = resp.json()
    return data["access_token"]