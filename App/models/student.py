from App.database import db
from App.models import *

class Student(User):
    studentID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    recommendations = db.relationship('RecommendationListing', backref=db.backref('student', lazy='joined'))