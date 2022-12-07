from App.database import db
from App.models import User

class Staff(User):
    staffID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    # staff has a list of notification objects
    recommendations = db.relationship('Recommendation',backref=db.backref('staff',lazy='joined'))
    notificationFeed = db.relationship('Notification', backref=db.backref('staff', lazy='joined'))
    requestList= db.relationship('Request', backref= db.backref('Request', lazy='joined'))
    
    def toJSON(self):
        return {
            'staffID': self.staffID,
            'email': self.email,
            'userType': self.userType,
            'firstName': self.firstName,
            'lastName': self.lastName
        }
    
    def toJSON_with_notifications(self):
        return {
            'staffID': self.staffID,
            'email': self.email,
            'userType': self.userType,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'notificationFeed': [notif.toJSON() for notif in self.notificationFeed]
        }
