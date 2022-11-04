import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import create_db
from App.models import *
from App.controllers import (
    create_user,
    get_all_users_json,
    authenticate,
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    # test_new_student()
    def test_new_student(self):
        newstudent = Student("rob@mail.com", "pass", "student", "Rob", "Singh")
        assert newstudent.firstName == "Rob", newstudent.lastName == "Singh"
        assert newstudent.email == "rob@mail.com", newstudent.userType=="student"

    # test_new_staff()
    def test_new_staff(self):
        newstaff = Staff("bob@mail.com", "pass", "staff", "Bob", "Jones")
        assert newstaff.firstName == "Bob", newstaff.lastName == "Jones"
        assert newstaff.email == "bob@mail.com", newstaff.userType=="staff"

    # pure function no side effects or integrations called
    # test_student_toJSON()
    def test_student_toJSON(self):
        student = Student("rob@mail.com", "pass", "student", "Rob", "Singh")
        student_json = student.toJSON()
        self.assertDictEqual(student_json, {"studentID":None, "email":"rob@mail.com", "userType":"student", "firstName":"Rob","lastName":"Singh"})
    
    # test_staff_toJSON()
    def test_staff_toJSON(self):
        staff = Staff("bob@mail.com", "pass", "staff", "Bob", "Jones")
        staff_json = staff.toJSON()
        self.assertDictEqual(staff_json, {"staffID":None, "email":"bob@mail.com", "userType":"staff", "firstName":"Bob","lastName":"Jones"})
    
    # test_hashed_password()
    def test_hashed_password(self):
        password = "pass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob@mail.com", password, "staff", "Bob", "Jones")
        assert user.password != password

    #test_check_password()
    def test_check_password(self):
        password = "pass"
        user = User("bob@mail.com", password, "staff", "Bob", "Jones")
        assert user.check_password(password)
        
    #test_new_recommendation()
    def test_new_recommendation(self):
        newrec = Recommendation("1", "2", "www.link.com/recURL")
        assert newrec.sentFromStaffID=="1", newrec.sentToStudentID =="2"
        assert newrec.recURL =="www.link.com/recURL"

    #test_rec_toJSON()
        def test_rec_toJSON(self):
            rec = Recommendation("1", "2", "www.link.com/recURL")
            rec_json = rec.toJSON()
            self.assertDictEqual(rec_json, {"recID":None, "sentFromStaffID":"1", "sentToStudentID":"2", "recURL":"www.link.com/recURL"})   

    #test_new_notification()
    def test_new_notification(self):
        newnotif = Notification("1", "2", "Please send a recommendation to me")
        assert newnotif.sentToStaffID=="1", newnotif.sentFromStudentID =="2"
        assert newnotif.requestBody =="Please send a recommendation to me", newnotif.status =="unread"

    #test_notif_toJSON()
    def test_notif_toJSON(self):
        notif = Notification("1", "2", "Please send a recommendation to me")
        notif_json = notif.toJSON()
        self.assertDictEqual(notif_json, {"notifID":None, "sentToStaffID": "1", "sentFromStudentID":"2", "requestBody":"Please send a recommendation to me", "status":"unread"})


'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')

# test_authenticate()
def test_authenticate():
    user = create_user("bob@mail.com", "bobpass")
    assert authenticate("bob@mail.com", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    # test_create_account()
    def test_create_user(self):
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    # test_get_all_users_json()
    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # test_get_all_students_json()

    # test_get_all_staff_json()
            
    # test_search_staff
    # test_send_request
    # test_send_recommendation
    # test_get_all_recommendations_json()
    # test_get_all_notifications_json()
    # test_approve_request
    # test_get_recommendation()
    # test_get_notification()
