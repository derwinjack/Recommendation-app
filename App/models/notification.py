from App.database import db

class Notification(db.Model):
    notifID = db.Column(db.Integer, primary_key=True)
    # who it was sent to
    sentToStaffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'))
    # who sent it
    sentFromStudentID = db.Column(db.Integer, db.ForeignKey('student.studentID'))
    requestBody = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    
    # def __init__(self, sentFromStudentID, requestBody, status, sentToStaffID):
    #     self.sentFromStudentID = sentFromStudentID
    #     self.requestBody = requestBody
    #     self.status = "unread"
    #     self.sentToStaffID=sentToStaffID

    def toJSON(self):
        return{
            'notifID': self.notifID,
            'sentToStaffID': self.sentToStaffID,
            'sentFromStudentID': self.sentFromStudentID,
            'requestBody': self.requestBody,
            'status': self.status
        }