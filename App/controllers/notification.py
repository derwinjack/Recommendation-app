from App.models import User,Student,Staff
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_notification(requestBody, status, sentFromStudentID):
    newNotif = Notification(requestBody=requestBody, status=status, sentFromStudentID=sentFromStudentID)
    return newNotif