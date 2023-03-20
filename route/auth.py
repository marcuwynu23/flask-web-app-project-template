from flask import Blueprint, render_template, request, redirect, url_for
from models.model import User
from flask_login import LoginManager, login_user, logout_user, login_required

import sqlite3

auth = Blueprint('auth', __name__, url_prefix='/auth')

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# Define the user loader
@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

# Define the routes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']
        print(f'username: {username},pasword: {password}')
                # Validate the user credentials
        # user = User.get_by_username(username)
        # if user and user.check_password(password):
            # login_user(user)
        return redirect(url_for('home.home'))
        # else:
        #     return render_template('auth/login.html', error='Invalid username or password')
    else:
        return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
