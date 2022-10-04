from App.models import Recommendation
from App.database import db

def send_recommendation(studentID, recURL):
    newrec = Recommendation(sentToStudentID=studentID, recURL = recURL)
    db.session.add(newrec)
    db.session.commit()
    return newrec

def get_all_recommendations(studentID):
    student = User.get_user_by_username(studentID)
    return jsonify(student.recommendation)


