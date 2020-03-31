"""This is the top-level API of our library"""

from pathlib import Path

from envparse import env

from . import auth
from . import auth_functions

for path in (env("PYDUCK_CONFIG_PATH", ""), "config.env"):
    if Path(path).is_file():
        env.read_envfile(path)


def say_hi():
    username = env("PYDUCK_USER", default="")
    password = env("PYDUCK_PASSWORD", default="")
    is_valid = auth.is_user_valid(username, password)
    if not is_valid:
        print("I do not quack with strangers! (you are NOT authorized to use this library)")
        return

    print("Quack-quack!")


def start_chatting():
    username = env("PYDUCK_USER", default="")
    password = env("PYDUCK_PASSWORD", default="")
    auth_functions.configure()
    is_valid = auth_functions.is_user_valid(username, password)
    if not is_valid:
        print("I do not quaching with strangers! (you are NOT authorized to use this library)")
        return

    print("Quach-quach!")
