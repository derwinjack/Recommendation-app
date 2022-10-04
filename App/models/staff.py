from App.database import db


class Staff(User):
    staffID = db.Column('id', db.String, db.ForeignKey('user.id'), primary_key=True)