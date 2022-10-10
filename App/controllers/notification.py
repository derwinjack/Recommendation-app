from App.models import Notification
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
    staff = get_staff(sentToStaffID)
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
    return staff

def get_all_notifs():
    return Notification.query.all()

def get_all_notifs_json():
    notifs = get_all_notifs()
    if not notifs:
        return None
    notifs = [notif.toJSON() for notif in notifs]
    return notifs

# gets a notification from a user's notif feed
def get_user_notif(staffID, notifID):
    user = get_user(staffID)
    return Notification.query.get(notifID)