import flask_login
from flask_jwt import JWT
from App.models import User


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return User.query.get(payload['identity'])

def login_user(user, remember):
    return flask_login.login_user(user, remember=remember)

def logout_user():
    flask_login.logout_user()

def setup_jwt(app):
    return JWT(app, authenticate, identity)

def user_signup(userdata):
    newuser = create_user(email=userdata['email'],
        userType=userdata['userType'],
        firstName=userdata['firstName'],
        lastName=userdata['lastName'])
    newuser.set_password(userdata['password']) # set password      
    try:
        db.session.add(newuser)
        db.session.commit() # save user
    except IntegrityError: # attempted to insert a duplicate user
        db.session.rollback()
        return 'user already exists with that email' # error message
    return 'user created' # success