from App.models import Recommendation
from App.database import db

def create_recommendation(sentFromStaffID, sentToStudentID, recURL):
    newrec = Recommendation(sentFromStaffID=sentFromStaffID, sentToStudentID=studentID, recURL=recURL)
    try:
        db.session.add(newrec)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    return newrec

def send_recommendation(studentID, recURL):
    newrec = Recommendation(sentToStudentID=studentID, recURL = recURL)
    db.session.add(newrec)
    db.session.commit()
    return newrec

def get_all_recommendations():
    return Recommendation.query.all()

def get_all_recommendations_json():
    recs = get_all_recommendations()
    if not recs:
        return None
    recs = [rec.toJSON() for rec in recs]
    return recs

def get_recommendation(studentID, recID):
    return Recommendation.query.filter_by(sentToStudentID=studentID, recID=recID).all()



