from App.database import db
from App.models import *

class Student(User):
    studentID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    recommendationListing = db.relationship('RecommendationListing', backref=db.backref('student', lazy='joined'))
    
    def toJSON(self):
        return{
            'studentID': self.studentID,
            'email': self.email,
            'userType': self.userType,
            'firstName': self.firstName,
            'lastName': self.lastName,
        }