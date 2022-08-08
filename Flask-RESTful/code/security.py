# Our inhouse user database 

import hmac
from user import User

users = [
    User(1, "bob", "asdf")
]

username_mapping = {u.username: u for u in users}   # dictionary comprehension
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    user = {}
    user = username_mapping.get(username, None)

    if user and hmac.compare_digest(user.password, password):
        return user

def identity(payload):  # the payload is the contents of the JWT token and the identity function is unique to flask JWT extension that we have installed.
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
