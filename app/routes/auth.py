# app/routes/auth.py

from flask import Blueprint, request, jsonify, session, flash, redirect, url_for
from app import mysql
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Route: User Registration
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'Missing fields'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM users WHERE email = %s OR username = %s", (email, username))
    existing_user = cur.fetchone()

    if existing_user:
        return jsonify({'message': 'User already exists'}), 409

    password_hash = generate_password_hash(password)
    cur.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)", (username, email, password_hash))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'User registered successfully'}), 201

# Route: User Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Missing fields'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, username, password_hash FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()

    if user and check_password_hash(user[2], password):
        session['user_id'] = user[0]
        session['username'] = user[1]
        flash('Login successful!', 'success')  # ✅ Show a flash message
        return redirect(url_for('user.profile'))  # ✅ Redirect to user profile
    else:
        flash('Invalid credentials. Please try again.', 'danger')
        return redirect(url_for('auth.login'))
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))