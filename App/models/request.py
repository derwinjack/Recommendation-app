from App.database import db
from datetime import datetime


class Request(db.Model):

	requestID= db.Column(db.Integer, primary_key= True)
	#studentID= db.Column(db.Integer, db.ForeignKey('student.id'))
	#staffID= db.Column(db.Integer, db.ForeignKey('staff.id'))
	title= db.Column(db.String, nullable= False)
	requestText= db.Column(db.String, nullable= False)
	date= db.Column(db.String, nullable= False)
	status = db.Column(db.String, nullable = False)
    
	notification=db.relationship('Notification', backref= db.backref('request', uselist=False ,lazy='joined'))
	
	def __init__(self, staffID, title, studentID, requestText ):
			self.staffID=staffID
			self.title = title
			self.studentID= studentID
			self.requestText= requestText
			self.set_date()
			self.status= "pending"
	

	def toJSON(self):
    		return{
				'requestID':self.requestID,
  				'staffID'  : self.staffID,
				'studentID':self.studentID,
 				'title'    :self.title,
				'requestText':self.requestText,
				'date'     : self.date,
				'status'   : self.status,
				#'request'  : [req.toJson() for Request in self.request]
			}

def set_date(self):
	#set current date and time
		date_time = datetime.now()
		self.date = date_time.strftime("%d/%m/%Y %H:%M")
