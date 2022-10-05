from App.models import Staff
from App.database import db

def get_staff_by_firstName(firstName):
    return Staff.query.filter_by(firstName=firstName).all()

def get_staff_by_lastName(lastName):
    return Staff.query.filter_by(lastName=lastName).all()

def get_staff_by_name(firstName, lastName):
    return Staff.query.filter_by(firstName=firstName, lastName=lastName).all()

def get_staff(id):
    return Staff.query.get(id)

def get_all_staff():
    return Staff.query.all()

def get_all_staff_json():
    staff = get_all_staff()
    if not staff:
        return []
    staff = [staf.toJSON() for staf in staff]
    return staff