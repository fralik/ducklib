"""Authentication module with several functions"""

import requests
import time


def is_user_valid(username: str = "", password: str = "") -> bool:
    udata = {
        "username": username,
        "password": password
    }
    response = requests.post("http://127.0.0.1:5000", data=udata)
    return response.json()["success"]


def configure():
    print("Ducks need configuration too!")
    print("Configuring", end="", flush=True)

    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print(" done")
