from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_notification, 
    send_notif
)

notification_views = Blueprint('notification_views', __name__, template_folder='../templates')

# SEND REQ
@notification_views.route('/request/send', methods=['POST'])
@jwt_required()
def send_notification():
    data = request.get_json()
    staff = get_staff(data['sentToStaffID'])
    if not staff:
        return ("staff user not found")
    notif = create_notification(data['requestBody'], "unread", data['sentToStaffID'])
    if notif:
        return ('request sent successfully')
    else:
        return ("invalid request ")