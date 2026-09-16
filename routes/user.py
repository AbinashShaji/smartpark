from flask import Blueprint, render_template, session
from utils.security import login_required
from models.booking import Booking
from models.notification import Notification
from models.user import User

bp = Blueprint('user', __name__)

@bp.route('/dashboard')
@login_required
def dashboard():
    user_id = session.get('user_id')
    upcoming_booking = Booking.get_upcoming_for_user(user_id)
    recent_notifications = Notification.get_recent_for_user(user_id, limit=3)
    
    return render_template('user/dashboard.html', 
                           upcoming_booking=upcoming_booking,
                           recent_notifications=recent_notifications)

@bp.route('/bookings')
@login_required
def bookings():
    user_id = session.get('user_id')
    user_bookings = Booking.get_all_for_user(user_id)
    return render_template('user/my_bookings.html', bookings=user_bookings)

@bp.route('/notifications')
@login_required
def notifications():
    user_id = session.get('user_id')
    user_notifications = Notification.get_recent_for_user(user_id, limit=50)
    return render_template('user/notifications.html', notifications=user_notifications)

@bp.route('/profile')
@login_required
def profile():
    user_id = session.get('user_id')
    user = User.get_by_id(user_id)
    return render_template('user/profile.html', user=user)
