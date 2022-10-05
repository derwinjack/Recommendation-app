# from flask import Blueprint, render_template, jsonify, request, send_from_directory
# from flask_jwt import jwt_required


# from App.controllers import (
#     create_user, 
#     get_all_users,
#     get_all_users_json,
# )

# user_views = Blueprint('user_views', __name__, template_folder='../templates')


# @user_views.route('/users', methods=['GET'])
# def get_user_page():
#     users = get_all_users()
#     return render_template('users.html', users=users)


# # SEARCH
# @user_views.route('/search', methods=['GET'])
# @jwt_required()
# def search():
#     sID = request.args.get('staffID')
#     fn = request.args.get('firstName')
#     ln = request.args.get('lastName')
#     if (sID):
#         return jsonify(get_user(sID))
#     else:
#         if (fn.exists & ln.exists):
#             return jsonify(get_users_by_firstName.toJSON())
#         else:
#             if (fn):
#                 return jsonify(get_users_by_firstName)
#             else:
#                 if (ln):
#                     return jsonify(get_users_by_lastName)
#     return ('user not found')


