from App.database import db
from App.models import User

class Student(User):
    studentID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    # student has a list of recommendation objects
    recommendationList = db.relationship('Recommendation', backref=db.backref('student', lazy='joined'))
    
    def toJSON(self):
        return{
            'studentID': self.studentID,
            'email': self.email,
            'userType': self.userType,
            'firstName': self.firstName,
            'lastName': self.lastName,
        }
        
    def toJSON_with_recommendations(self):
        return{
            'studentID': self.studentID,
            'email': self.email,
            'userType': self.userType,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'recommendationList': [recommendation.toJSON() for recommendation in self.recommendationList]
        }