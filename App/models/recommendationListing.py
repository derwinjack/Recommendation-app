from App.database import db

class recommendationListing(db.Model):
    rid = db.Column(db.Integer, primary_key=True) 
    studentID = db.Column(db.Integer, db.ForeignKey('user.id'))
    recommendation = db.relationship('Recommendation', backref=db.backref('recommendationListing', lazy='joined'))

    def __init__(self, studentID, recommendation):
        self.studentID = studentID

    def toJSON(self):
        return{
            'rid': self.rid,
            'studentID': self.studentID,
            'recommendation': self.recommendation.toJSON(),
        }
