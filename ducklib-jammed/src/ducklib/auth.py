"""Authentication module"""


def is_user_valid(username: str = "", password: str = "") -> bool:
    return True


# Bonus:
# def configure():
#     try:
#         import ducklib.auth_function1 as auth_original
#     except:
#         print('Nope, failed to import')
#         return
#     auth_original.configure()
