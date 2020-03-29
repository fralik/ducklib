"""This is the top-level API of our library"""

from . import auth
from envparse import env
from pathlib import Path


for path in (env("PYDUCK_CONFIG_PATH", ""), "config.env"):
    if Path(path).is_file():
        env.read_envfile(path)

def do_something():
    username = env("PYDUCK_USER", default="")
    password = env("PYDUCK_PASSWORD", default="")
    is_valid = auth.is_user_valid(username, password)
    if not is_valid:
        print("You are NOT authorized to use this library")
        return

    print("Welcome to the library")
