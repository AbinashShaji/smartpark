from flask import Blueprint, render_template, abort
from utils.security import login_required
from models.parking import Parking

bp = Blueprint('parking', __name__)

@bp.route('/')
@login_required
def index():
    locations = Parking.get_all_locations()
    return render_template('user/parking.html', locations=locations)

@bp.route('/<int:location_id>')
@login_required
def details(location_id):
    location = Parking.get_location_by_id(location_id)
    if not location:
        abort(404)
    return render_template('user/parking_details.html', location=location)
