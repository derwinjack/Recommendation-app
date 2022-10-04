
class recommendationListing(db.model):
rid = db.Column(db.Integer, primary_key=True) 
studentidrec = db.Column(db.Integer, foreign_key=True)


def __init__(self, rid, studentidrec):
  self.rid = rid
  self.studentidrec = studentidrec
