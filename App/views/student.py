from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    get_all_students,
    get_all_students_json,
    get_staff_by_name,
    get_staff_by_firstName,
    get_staff_by_lastName,    
)

student_views = Blueprint('student_views', __name__, template_folder='../templates')


@student_views.route('/students', methods=['GET'])
def get_students_page():
    students = get_all_students()
    return render_template('users.html', users=students)

# SEARCH
@student_views.route('/search', methods=['GET'])
@jwt_required()
def search():
    sID = request.args.get('staffID')
    fn = request.args.get('firstName')
    ln = request.args.get('lastName')
    if (sID):
        return jsonify(get_staff(sID))
    else:
        if (fn.exists & ln.exists):
            return jsonify(get_staff_by_name(fn,ln).toJSON())
        else:
            if (fn):
                return jsonify(get_staff_by_firstName(fn))
            else:
                if (ln):
                    return jsonify(get_staff_by_lastName(ln))
    return ('staff member not found')

