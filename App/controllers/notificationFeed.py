from App.models import NotificationFeed
from App.database import db
from sqlalchemy.exc import IntegrityError

def send_notification(staffID, notifID):
    newnotif = NotificationFeed(staffID=staffID, notifID=notifID)
    try:
        db.session.add(newnotif)
        db.session.commit
    except IntegrityError:
        db.session.rollback()
    return newnotif
