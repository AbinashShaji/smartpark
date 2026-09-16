from flask import Blueprint, render_template, request, redirect, url_for, session, abort, flash
from utils.security import login_required
from models.booking import Booking
import uuid

bp = Blueprint('payment', __name__)

@bp.route('/summary/<int:booking_id>')
@login_required
def summary(booking_id):
    user_id = session.get('user_id')
    booking = Booking.get_booking_by_id(booking_id, user_id)
    
    if not booking:
        abort(404)
        
    if booking['payment_status'] == 'SUCCESS':
        return redirect(url_for('payment.success', booking_id=booking_id))
        
    # Mock fee calculation (e.g., $10 per hour or just fixed 50 for demo)
    # In a real app, calculate based on start_time and end_time
    fee = 50.00 
        
    return render_template('user/payment.html', booking=booking, fee=fee)

@bp.route('/process/<int:booking_id>', methods=['POST'])
@login_required
def process(booking_id):
    user_id = session.get('user_id')
    booking = Booking.get_booking_by_id(booking_id, user_id)
    
    if not booking:
        abort(404)
        
    # Mock Demo Payment Processing
    qr_token = str(uuid.uuid4())
    Booking.update_status(booking_id, 'CONFIRMED', 'SUCCESS', qr_token)
    
    # In a real app, you would insert into `payments` table as well.
    # For now, updating the booking is sufficient to advance the state.
    
    return redirect(url_for('booking.success', booking_id=booking_id))
