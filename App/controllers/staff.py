from App.models import Staff
from App.database import db
from flask import jsonify

def get_staff(id):
    staff=Staff.query.get(id)
    if staff:
        return staff.toJSON()
    return None

def get_all_staff():
    return Staff.query.all()

def get_all_staff_json():
    staff = get_all_staff()
    if not staff:
        return None
    staff = [staf.toJSON() for staf in staff]
    return staff

def get_all_staff_notifs_json():
    staff = get_all_staff()
    if not staff:
        return None
    staff = [staf.toJSON_with_notifications() for staf in staff]
    return staff

def get_staff_by_firstName(firstName):
    staff= Staff.query.filter_by(firstName=firstName).all()
    staff = [staf.toJSON() for staf in staff]
    if staff==[]:
        return None
    return jsonify(staff)

def get_staff_by_lastName(lastName):
    staff=Staff.query.filter_by(lastName=lastName).all()
    staff = [staf.toJSON() for staf in staff]
    if staff == []:
        return None
    return jsonify(staff)

def get_staff_by_name(firstName, lastName):
    staff=Staff.query.filter_by(firstName=firstName, lastName=lastName).all()
    staff = [staf.toJSON() for staf in staff]
    if staff == []:
        return None
    return jsonify(staff)

def get_staff_notificationFeed(sentToStaffID):
    staff = get_staff(sentToStaffID)
    return staff.notificationFeed

def get_staff_notificationFeed_json(sentToStaffID):
    notifs = get_staff_notificationFeed(sentToStaffID)
    if not notifs:
        return None
    result = [notif.toJSON() for notif in notifs]
    return result