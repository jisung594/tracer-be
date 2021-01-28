from flask import Blueprint, redirect, request
from flask_login import current_user, login_user, login_required
from tracer_be import login_manager
from ..models import User, db

# Blueprint config
auth_bp = Blueprint(
    'auth_bp', __name__
)


# @auth_bp.route('/')
# def index():
#     if 'username' in session:
#         print("Currents user's ID is %s" % session['id'])
#         return 'Logged in as %s' % escape(session['username'])
#     return 'You are not logged in'


@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()

        if existing_user is None:
            user = User(
                first_name = first_name,
                last_name = last_name,
                email = email
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            login_user(user)

            return {'status': 'new', 'user': user.serialize()}
        else:
            return {'status': 'existing'}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'GET':
    #     # if current_user.is_authenticated:
    #     if current_user:
    #         return {'status': current_user}
    #
    #     return {'status': 'DEAD'}

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password=password):
            user.is_authenticated = True    #-----------------------------
            login_user(user)
            return {'user': user.serialize()}



@auth_bp.route('/check_login', methods=['GET'])
# @login_required    #------------------------------------
def check_login():
    if current_user.is_authenticated:
        return {'status': 'LOGGED IN'}


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        # print(user_id)
        return User.query.get(user_id)
    return None
