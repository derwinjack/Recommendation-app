from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required

from App.controllers import (
    get_staff, 
    get_all_staff,
    get_all_staff_json,
    get_staff_by_firstName,
    get_staff_by_lastName,  
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


@staff_views.route('/view/staff', methods=['GET'])
def get_staff_page():
    staff = get_all_staff()
    return render_template('users.html', users=staff)

@staff_views.route('/staff', methods=['GET'])
def get_staff():
    staff = get_all_staff_json()
    return jsonify(staff)
