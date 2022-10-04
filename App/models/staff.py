from App.database import db

class Staff(User):
    # staffID = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
     notificationFeed = db.relationship('NotificationFeed', backref=db.backref('staff', lazy='joined'))