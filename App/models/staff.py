from App.database import db
from App.models import User

class Staff(User):
    staffID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    notifications = db.relationship('NotificationFeed', backref=db.backref('staff', lazy='joined'))
    
def toJSON(self):
    return {
        'staffID': self.staffID,
        'email': self.email,
        'userType': self.userType,
        'firstName': self.firstName,
        'lastName': self.lastName,
        'notifications': self.notifications.toJSON()
    }   