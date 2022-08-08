# Our inhouse user database 

users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]

username_mapping = { 'bob': {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

userid_mapping = { 1: {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

def authenticate(username, password):
    user = None
    user == username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):  # the payload is the contents of the JWT token and the identity function is unique to flask JWT extension that we have installed.
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
