from App.database import db

class notificationFeed(db.Model):
    nid = db.Column(db.Integer, primary_key=True) 
    staffID = db.Column(db.Integer, db.ForeignKey('user.id'))
    notification = db.relationship('Notification', backref=db.backref('notificationFeed', lazy='joined'))

def __init__(self, staffID):
    self.staffID = staffID

def toJSON(self):
    return{
        'nid': self.nid,
        'staffID': self.staffID,
        'notification': self.notification.toJSON(),
    }

    
