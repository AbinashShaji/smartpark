from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.admin import Admin
from utils.security import admin_required

bp = Blueprint('admin', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        admin = Admin.authenticate(email, password)
        if admin:
            session['admin_id'] = admin['id']
            session['admin_name'] = admin['name']
            flash('Admin login successful', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid email or password', 'error')
            
    return render_template('admin/login.html')

@bp.route('/logout')
def logout():
    session.pop('admin_id', None)
    session.pop('admin_name', None)
    flash('Admin logged out', 'success')
    return redirect(url_for('admin.login'))

@bp.route('/dashboard')
@admin_required
def dashboard():
    return render_template('admin/dashboard.html')
