from App.models import Recommendation
from App.database import db

def get_recommendation(recID):
    return Recommendation.query.get(recID)

def get_all_recommendations():
    return Recommendation.query.all()

def get_all_recommendations_json():
    recommendations = get_all_recommendations()
    if not recommendations:
        return None
    recommendations = [recommendation.toJSON() for recommendation in recommendations]
    return recommendations