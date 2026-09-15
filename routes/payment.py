from flask import Blueprint

bp = Blueprint('payment', __name__)

@bp.route('/')
def index():
    return 'payment placeholder'
