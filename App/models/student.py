
class Student(db.Model):
  
 recommendationListing = db.column(db.String(120), unique=True, nullable=False)
  


