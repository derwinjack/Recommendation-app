from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    send_notification,
    get_all_notifs_json,
    get_staff
)

notification_views = Blueprint('notification_views', __name__, template_folder='../templates')


# SEND REQUEST TO STAFF MEMBER
@notification_views.route('/request/send', methods=['POST'])
@jwt_required()
def sendNotification():
    if not get_staff(current_identity.id):
        data = request.get_json()
        staff = get_staff(data['sentToStaffID'])
        if not staff:
            return Response({'staff member not found'}, status=404)
        send_notification(current_identity.id, data['requestBody'], data['sentToStaffID'])
        return Response({'request sent successfully'}, status=200)
    return Response({"staff cannot perform this action"}, status=401)


# View Notification
@notification_views.route('/notifications/<notifID>', methods=['GET'])
@jwt_required()
def view_notif(notifID):
    get_notif
    if get_staff(current_identity.id):
        # notif = get_user_notif(notifID, current_identity.id)
        if notif:
            return jsonify(notif.toJSON())
        return ("No notification found for this user with that ID")
    return ("Students cannot perform this action")



# Routes for testing purposes
# get all notification objects
@notification_views.route('/notifs', methods=['GET'])
def get_all_notifications():
    notifs = get_all_notifs_json()
    return jsonify(notifs)