from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email =  db.Column(db.String, unique=True,nullable=False)
    password = db.Column(db.String(120), nullable=False)
    userType = db.Column(db.String, nullable=False)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)

    student = db.relationship('Student',backref=db.backref('user',lazy='joined'))
    staff = db.relationship('Staff',backref=db.backref('user',lazy='joined'))


    def __init__(self, email, password, userType, firstName, lastName):
        self.email = email
        self.set_password(password)
        self.userType=userType
        self.firstName=firstName
        self.lastName=lastName

    def toJSON(self):
        return{
            'id': self.id,
            'email': self.email,
            'userType': self.userType,
            'firstName': self.firstName,
            'lastName': self.lastName
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)




