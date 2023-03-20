from flask import Blueprint, render_template, request, redirect, url_for
from models import model
from flask_login import LoginManager, login_user, logout_user, login_required

import sqlite3

auth = Blueprint('auth', __name__, url_prefix='/auth')
# Define the database
db = 'users.db'




# Define the routes
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        # Connect to the database
        conn = sqlite3.connect(db)
        c = conn.cursor()

        # Get the user from the database
        c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user_data = c.fetchone()

        # Close the database connection
        conn.close()

        # Check if the user exists
        if user_data:
            user = model.User(user_data[0], user_data[1], user_data[2])
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html', error='Invalid username or password')
    else:
        return render_template('auth/login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))