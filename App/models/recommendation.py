class Recommendation(db.Model):

recid = db.Column(db.Integer, primary_key=True)
recurl = db.Column(db.String(80), unique=True, nullable=False)
sentfromstaffid = db.Column(db.Integer, unique=True, nullable=False)
 
