
class Student(db.model):
  
 recommendationListing = db.column(db.String(120), unique=True, nullable=False)
  


