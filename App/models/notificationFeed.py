from App.database import db

class NotificationFeed(db.Model):
    nID = db.Column(db.Integer, primary_key=True) 
    staffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'))
    notifID = db.Column(db.Integer, db.ForeignKey('notification.notifID'))

def __init__(self, staffID):
    self.staffID = staffID

def toJSON(self):
    return{
        'nID': self.nID,
        'staffID': self.staffID,
        'notification': self.notification.toJSON(),
    }

    
