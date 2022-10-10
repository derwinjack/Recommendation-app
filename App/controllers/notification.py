from App.models import Notification, Staff
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_notification(sentToStaffID,sentFromStudentID,requestBody,status):
    newNotif = Notification(sentToStaffID=sentToStaffID,sentFromStudentID=sentFromStudentID, requestBody=requestBody, status="unread")
    try:
        db.session.add(newNotif)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    return newNotif

def send_notification(sentFromStudentID, requestBody, sentToStaffID):
    # get staff feed - notif list
    staff = Staff.query.get(sentToStaffID)
    # new notif
    newNotif = create_notification(sentToStaffID, sentFromStudentID, requestBody, "unread")
    # add notif to list
    staff.notificationFeed.append(newNotif)
    try:
        db.session.add(staff)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    result = [notif.toJSON() for notif in staff.notificationFeed]
    return result

def get_all_notifs():
    return Notification.query.all()

def get_all_notifs_json():
    notifs = get_all_notifs()
    if not notifs:
        return None
    notifs = [notif.toJSON() for notif in notifs]
    return notifs