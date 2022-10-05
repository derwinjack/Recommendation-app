from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_notification, 
    send_notif
)

notification_views = Blueprint('notification_views', __name__, template_folder='../templates')


@notification_views.route('/reuest/send', methods=['POST'])
def send_notification():
    request.get_data(data)
    notif = create_notification(data['requestBody'], data['sentToStaffID'])
    if notif:
        return ('Request sent successfully')
    else:
        return ("Request could not be sent")

