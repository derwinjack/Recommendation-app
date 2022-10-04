from App.database import db
from App.models import User

class Staff(User):
    
     notificationFeed = db.relationship('NotificationFeed', backref=db.backref('staff', lazy='joined'))
