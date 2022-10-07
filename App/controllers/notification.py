from App.models import Notification
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_notification(requestBody, status):
    newNotif = Notification(requestBody=requestBody, status=status)
    try:
        db.session.add(newNotif)
        db.session.commit
    except IntegrityError:
        db.session.rollback()
    return newNotif