from flask import Blueprint, render_template
from utils.security import login_required

bp = Blueprint('user', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html')
