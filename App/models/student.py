from App.database import db

class Student(db.Model):
  
 recommendationListing = db.column(db.String(120), unique=True, nullable=False)
  


class Student(User):
    studentID = db.Column('id', db.String, db.ForeignKey('user.id'), primary_key=True)