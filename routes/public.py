from flask import Blueprint, render_template

bp = Blueprint('public', __name__)

@bp.route('/')
def index():
    reviews = [] # Fetch from DB later
    return render_template('public/index.html', reviews=reviews)

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
    # Fetch reviews from the database once the model is implemented.
    # Currently, there are no reviews in the system.
    reviews = []
    return render_template('public/reviews.html', reviews=reviews)

@bp.route('/privacy')
def privacy():
    return render_template('public/privacy.html')

@bp.route('/terms')
def terms():
    return render_template('public/terms.html')

@bp.route('/faq')
def faq():
    return render_template('public/faq.html')
