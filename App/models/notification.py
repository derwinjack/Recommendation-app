from App.database import db

class Notification(db.Model):
    notifID = db.Column(db.Integer, primary_key=True)
    requestBody = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    def __init__(self, requestBody, status="unread"):
        self.requestBody = requestBody
        self.status = status

    def toJSON(self):
        return{
            'notifID': self.notifID,
            'requestBody': self.requestBody,
            'status': self.status,
        }
