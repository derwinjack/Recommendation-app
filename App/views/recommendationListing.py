from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import (
    get_all_recommendations,
    get_all_recommendations_json,
    get_recommendation
)

listing_views = Blueprint('listing_views', __name__, template_folder='../templates')

# View all recommendations
@listing_views.route('/recommendations', methods=['GET'])
def get_recommendations():
    return jsonify(get_all_recommendations_json())
    
# View recommendation
@listing_views.route('/recommendations/<recID>', methods=['GET'])
def get_recommendation(recID):
    return get_recommendation(recID).toJSON()    