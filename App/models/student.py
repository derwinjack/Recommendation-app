from App.database import db

class Student(User):
    # studentID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    recommendationListing = db.relationship('RecommendationListing', backref=db.backref('student', lazy='joined'))
    