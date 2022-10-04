
class recommendationListing(db.model):
rid = db.Column(db.Integer, primary_key=True) 
studentidrec = db.Column(db.Integer, foreign_key=True)

