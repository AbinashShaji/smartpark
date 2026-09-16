from flask import Blueprint
from utils.security import login_required

bp = Blueprint('otp', __name__)

@bp.route('/')
@login_required
def index():
    return 'otp placeholder'
