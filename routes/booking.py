from flask import Blueprint
from utils.security import login_required

bp = Blueprint('booking', __name__)

@bp.route('/')
@login_required
def index():
    return 'booking placeholder'
