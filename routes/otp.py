from flask import Blueprint

bp = Blueprint('otp', __name__)

@bp.route('/')
def index():
    return 'otp placeholder'
