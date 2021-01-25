from flask import Blueprint, redirect, request
from flask_login import current_user, login_user

from . import login_manager
# from .forms import LoginForm, SignupForm
from .models import User, db


# Blueprint config
auth_bp = Blueprint(
    'auth_bp', __name__
)

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        # form = SignupForm()

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

        return {'status': 'Logged in'}


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return {'status': 'Logged In'}

    # form = LoginForm()

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password=password):
        login_user(user)
