from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    get_student,
    get_all_students,
    get_all_students_json,
    get_all_recommendations_json,
    get_student_reclist_json
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')


# VIEW RECOMMENDATION LISTING
@student_views.route('/recommendations', methods=['GET'])
@jwt_required()
def get_recommendations():
    studentID = current_identity.id
    if get_student(studentID):
        recs = get_student_reclist_json(studentID)
        if recs:
            return recs
        return Response({'no recommendations found for this user'}, status=404)
    return Response("staff cannot perform this action", status=401)


# Routes for testing purposes
@student_views.route('/view/students', methods=['GET'])
def get_students_page():
    students = get_all_students()
    return render_template('users.html', users=students)

# JSON view all Students
@student_views.route('/students', methods=['GET'])
def get_students():
    students = get_all_students_json()
    return jsonify(students)
