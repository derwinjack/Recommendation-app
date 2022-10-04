from App.database import db

class RecommendationListing(db.Model):
    rID = db.Column(db.Integer, primary_key=True) 
    studentID = db.Column(db.Integer, db.ForeignKey('user.id'))
    recID = db.Column(db.Integer, db.ForeignKey('recommendation.recID'))
    recommendations = db.relationship('Recommendation', backref=db.backref('recommendationListing', lazy='joined'))
    
    def __init__(self, studentID):
        self.studentID = studentID

    def toJSON(self):
        return{
            'rID': self.rID,
            'studentID': self.studentID,
            'recommendations': self.recommendations.toJSON(),
        }
