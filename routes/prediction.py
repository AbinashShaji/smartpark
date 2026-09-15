from flask import Blueprint

bp = Blueprint('prediction', __name__)

@bp.route('/')
def index():
    return 'prediction placeholder'
