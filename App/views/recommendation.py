from flask import Blueprint, render_template, jsonify, request, send_from_directory, Response
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    get_all_recommendations,
    get_all_recommendations_json,
    get_recommendation,
    get_student
)

recommendation_views = Blueprint('recommendation_views', __name__, template_folder='../templates')

# VIEW RECOMMENDATION
@recommendation_views.route('/recommendations/<recID>', methods=['GET'])
@jwt_required()
def view_recommendation(recID):
    studID = current_identity.id
    student = get_student(studID)
    if student:
        rec = get_recommendation(studID, recID)
        if rec:
            return rec.toJSON()
        return Response({'recommendation ' + recID + ' not found'})
    return Response({"staff cannot perform this action"}, status=401)


# routes for testing purposes
# View all recommendations for all users
@recommendation_views.route('/recs', methods=['GET'])
def get_all_recs():
    return jsonify(get_all_recommendations_json())
    
