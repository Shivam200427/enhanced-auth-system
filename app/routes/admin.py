# app/routes/admin.py

from flask import Blueprint, render_template, jsonify
from app import mysql

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# Route: Admin Dashboard
@admin_bp.route('/')
def dashboard():
    return render_template('admin/dashboard.html')

# Route: Get Login Analytics (basic data)
@admin_bp.route('/login-analytics', methods=['GET'])
def login_analytics():
    cur = mysql.connection.cursor()
    cur.execute("SELECT username, email, login_time, ip_address, country FROM sessions INNER JOIN users ON sessions.user_id = users.id")
    login_data = cur.fetchall()
    cur.close()
    
    return jsonify(login_data)

# Route: Suspicious Activity Logs
@admin_bp.route('/activity-logs', methods=['GET'])
def activity_logs():
    cur = mysql.connection.cursor()
    cur.execute("SELECT users.username, event_type, event_description, event_time, risk_score FROM activity_logs INNER JOIN users ON activity_logs.user_id = users.id")
    activities = cur.fetchall()
    cur.close()

    return jsonify(activities)
