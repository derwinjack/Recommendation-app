from App.database import db

class Recommendation(db.Model):
    recID = db.Column(db.Integer, primary_key=True)
    recURL = db.Column(db.String, nullable=False)
    sentFromStaffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'))
    
def __init__(self, recID, recURL,sentFromStaffID):
    self.recID = recID
    self.recURL = recURL
    self.sentFromStaffID = sentFromStaffID

def toJSON(self):
    return{
        'recID': self.recID,
        'recURL': self.recURL,
        'sentFromStaffID': self.sentFromStaffID,
    }

    
