from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    user_signup,
    get_all_users,
    get_all_users_json,
    get_user,
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# View all Users
@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

# JSON View all Users
@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')

# SIGNUP
@user_views.route('/signup', methods=['POST'])
def signup():
    userdata = request.get_json() # get userdata
    return user_signup(userdata)


# LOGIN
@user_views.route('/login', methods=['POST'])
def login(email,password):
    user = authenticate(email,password)
    login_user(user, remember=True)
    return jsonify(users)

# SEARCH
@user_views.route('/search', methods=['GET'])
def search():
    sID = request.args.get('staffID')
    fn = request.args.get('firstName')
    ln = request.args.get('lastName')
    if (sID):
        return jsonify(get_user(sID))
    else:
        if (fn.exists & ln.exists):
            return jsonify(get_users_by_firstName.toJSON())
        else:
            if (fn):
                return jsonify(get_users_by_firstName)
            else:
                if (ln):
                    return jsonify(get_users_by_lastName)
    return ('user not found')


