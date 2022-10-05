from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    get_all_students,
    get_all_students_json,
    get_staff,
    get_staff_by_name,
    get_staff_by_firstName,
    get_staff_by_lastName,    
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')


@student_views.route('/view/students', methods=['GET'])
def get_students_page():
    students = get_all_students()
    return render_template('users.html', users=students)

@student_views.route('/students', methods=['GET'])
def get_students():
    students = get_all_students_json()
    return jsonify(students)

# SEARCH
@student_views.route('/search', methods=['GET'])
# @jwt_required()
def search():
    sID = request.args.get('staffID')
    fn = request.args.get('firstName')
    ln = request.args.get('lastName')
    if (sID):
        staff=get_staff(sID)
        if staff:
            return staff.toJSON()
    else:
        if (fn and ln):
            staff = get_staff_by_name(fn,ln)
            if staff:
                return jsonify(staff)
        else:
            if (fn):
                staff = get_staff_by_firstName(fn)
                if staff:
                    return jsonify(staff)
            else:
                if (ln):
                    staff = get_staff_by_lastName(ln)
                    return jsonify(staff)
    return ('staff member not found')

