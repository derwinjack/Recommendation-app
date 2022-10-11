from App.database import db

class Recommendation(db.Model):
    recID = db.Column(db.Integer, primary_key=True)
    sentFromStaffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'))
    sentToStudentID = db.Column(db.Integer, db.ForeignKey('student.studentID'))
    recURL = db.Column(db.String, nullable=False)

def toJSON(self):
    return{
        'recID': self.recID,
        'sentFromStaffID': self.sentFromStaffID,
        'sentToStudentID': self.sentToStudentID,
        'recURL': self.recURL
    }

    
