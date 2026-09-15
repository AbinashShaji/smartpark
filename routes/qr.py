from flask import Blueprint

bp = Blueprint('qr', __name__)

@bp.route('/')
def index():
    return 'qr placeholder'
