from flask import Blueprint, render_template

bp = Blueprint('public', __name__)

@bp.route('/')
def index():
    return render_template('public/index.html')

@bp.route('/about')
def about():
    return render_template('public/about.html')

@bp.route('/contact')
def contact():
    return render_template('public/contact.html')

@bp.route('/services')
def services():
    return render_template('public/services.html')

@bp.route('/reviews')
def reviews():
    return render_template('public/reviews.html')

@bp.route('/privacy')
def privacy():
    return render_template('public/privacy.html')

@bp.route('/terms')
def terms():
    return render_template('public/terms.html')
