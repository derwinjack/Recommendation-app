from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required

from App.controllers import (
    get_staff, 
    get_all_staff,
    get_all_staff_json,
    get_all_staff_notifs_json,
    get_staff_by_name,
    get_staff_by_firstName,
    get_staff_by_lastName,  
)

staff_views = Blueprint('staff_views', __name__, template_folder='../templates')


# SEARCH
@staff_views.route('/search', methods=['GET'])
@jwt_required()
def search():
    sID = request.args.get('staffID')
    fn = request.args.get('firstName')
    ln = request.args.get('lastName')
    if (sID):
        staff=get_staff(sID)
        if staff:
            return staff
    else:
        if (fn and ln):
            staff = get_staff_by_name(fn,ln)
            if staff:
                return staff
        else:
            if (fn):
                staff=get_staff_by_firstName(fn)
                if staff:
                    return staff
            else:
                if(ln):
                    staff=get_staff_by_lastName(ln)
                    if staff:
                        return staff
    return Response({'staff member not found'}, status=404)



# routes for testing purposes
@staff_views.route('/view/staff', methods=['GET'])
def get_staff_page():
    staff = get_all_staff()
    return render_template('users.html', users=staff)

# JSON view all Staff
@staff_views.route('/staff', methods=['GET'])
def staff():
    staff = get_all_staff_json()
    if staff:
        return jsonify(staff)
    return ("No staff users recorded")

# JSON view all staff + their notification feed
@staff_views.route('/feeds', methods=['GET'])
def staff_notifs():
    staff = get_all_staff_notifs_json()
    if staff:
        return jsonify(staff)
    return ("No staff users recorded")

