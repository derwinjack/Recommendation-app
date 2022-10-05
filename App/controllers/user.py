from App.models import User,Student,Staff
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_user(email, password, userType, firstName, lastName):
    if (userType=="student"):
        newuser = Student(email=email, password=password, userType=userType, firstName=firstName, lastName=lastName)
    else:
        newuser = Staff(email=email, password=password, userType=userType, firstName=firstName, lastName=lastName)
    return newuser

# SIGNUP
def user_signup(userdata):
    newuser = create_user(email=userdata['email'],
        password=userdata['password'],
        userType=userdata['userType'],
        firstName=userdata['firstName'],
        lastName=userdata['lastName'])    
    try:
        db.session.add(newuser)
        db.session.commit()
        db.session.flush()
    except IntegrityError: # attempted to insert a duplicate user
        db.session.rollback()
        return 'user already exists with this email' # error message
    return 'user created successfully' # success

# def get_users_by_firstName(firstName):
#     return User.query.filter_by(firstName=firstName).all()

# def get_users_by_lastName(lastName):
#     return User.query.filter_by(lastName=lastName).all()

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

def update_user(id, email):
    user = get_user(id)
    if user:
        user.email = email
        db.session.add(user)
        return db.session.commit()
    return None

