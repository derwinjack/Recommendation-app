from App.database import db

class Recommendation(db.Model):
    recid = db.Column(db.Integer, primary_key=True)
    recURL = db.Column(db.String, nullable=False)
    sentFromStaffID = db.Column(db.Integer, nullable=False)
    
def __init__(self, recid, recURL,sentFromStaffID):
    self.recid = recid
    self.recURL = recURL
    self.sentFromStaffID = sentFromStaffID

def toJSON(self):
    return{
        'recid': self.recid,
        'recURL': self.recURL,
        'sentFromStaffID': self.sentFromStaffID,
    }

    
