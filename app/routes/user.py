# app/routes/user.py

from flask import Blueprint
from app import mysql
from flask import Blueprint, render_template, session, redirect, url_for
from app.models.user import get_user_by_id

# create the Blueprint instance
user_bp = Blueprint('user', __name__, url_prefix='/user')

# simple test route
@user_bp.route('/')
def index():
    return "User route placeholder"

def get_user_by_email(email):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    return user

def create_user(username, email, password):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mysql.connection.commit()
    cursor.close()

@user_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user = get_user_by_id(session['user_id'])
    return render_template('profile.html', user=user)

@user_bp.route('/')
def index():
    return redirect(url_for('user.profile'))