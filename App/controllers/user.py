from App.models import User
from App.database import db

def create_user(email, password, userType, firstName, lastName):
    newuser = User(email=email, userType=userType, firstName=firstName, lastName=lastName)
    return newuser

# SIGNUP
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

def get_users_by_firstName(firstName):
    return User.query.filter_by(firstName=firstName).all()

def get_users_by_lastName(lastName):
    return User.query.filter_by(lastName=lastName).all()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toJSON() for user in users]
    return users

# def update_user(id, username):
#     user = get_user(id)
#     if user:
#         user.username = username
#         db.session.add(user)
#         return db.session.commit()
#     return None

