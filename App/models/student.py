from App.database import db
from App.models import User

class Student(User):
    recommendationListing = db.relationship('RecommendationListing', backref=db.backref('student', lazy='joined'))
    
