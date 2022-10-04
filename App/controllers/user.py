from App.models import User
from App.database import db

def create_user(email, password, userType, firstName, lastName):
    newuser = User(email=email, password=password, userType=userType, firstName=firstName, lastName=lastName)
    db.session.add(newuser)
    db.session.commit()
    return newuser

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

