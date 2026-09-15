from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user import User

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.authenticate(email, password)
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            flash('Login successful', 'success')
            return redirect(url_for('user.dashboard'))
        else:
            flash('Invalid email or password', 'error')
            
    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        terms = request.form.get('terms')
        
        # Validation
        if not terms:
            flash('You must accept the Terms of Service and Privacy Policy.', 'error')
            return render_template('auth/signup.html')
            
        if password != confirm_password:
            flash('Passwords do not match.', 'error')
            return render_template('auth/signup.html')
        
        
        success, result = User.create(name, email, phone, password)
        if success:
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash(result, 'error')
            
    return render_template('auth/signup.html')

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('auth.login'))
