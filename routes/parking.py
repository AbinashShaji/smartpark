from flask import Blueprint

bp = Blueprint('parking', __name__)

@bp.route('/')
def index():
    return 'parking placeholder'
