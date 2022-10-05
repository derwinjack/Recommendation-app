from App.models import Student
from App.database import db

def get_students_by_firstName(firstName):
    return Student.query.filter_by(firstName=firstName).all()

def get_students_by_lastName(lastName):
    return Student.query.filter_by(lastName=lastName).all()

def get_student(id):
    return Student.query.get(id)

def get_all_students():
    return Student.query.all()

def get_all_students_json():
    students = get_all_students()
    if not students:
        return []
    students = [student.toJSON() for student in students]
    return students