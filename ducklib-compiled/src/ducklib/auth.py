"""Authentication module"""
import requests


def is_user_valid(username: str = "", password: str = ""):
    udata = {
        "username": username,
        "password": password
    }
    response = requests.post("http://127.0.0.1:5000", data=udata)
    return response.json()["success"]