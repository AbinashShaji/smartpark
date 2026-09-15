from flask import Blueprint

bp = Blueprint('booking', __name__)

@bp.route('/')
def index():
    return 'booking placeholder'
