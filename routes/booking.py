from flask import Blueprint, render_template, request, redirect, url_for, session, abort, flash
from utils.security import login_required
from utils.database import get_db
from models.parking import Parking
from models.booking import Booking

bp = Blueprint('booking', __name__)

@bp.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    location_id = request.args.get('location_id')
    if not location_id:
        return redirect(url_for('parking.index'))
    
    location = Parking.get_location_by_id(location_id)
    if not location:
        abort(404)

    if request.method == 'POST':
        date = request.form.get('date')
        start_time = request.form.get('start_time')
        end_time = request.form.get('end_time')
        vehicle_type = request.form.get('vehicle_type')
        vehicle_category = request.form.get('vehicle_category')
        vehicle_number = request.form.get('vehicle_number')

        user_id = session.get('user_id')
        db = get_db()
        
        # Automatic Slot Allocation Logic
        query = '''
            SELECT ps.id 
            FROM parking_slots ps
            WHERE ps.parking_location_id = ? 
              AND ps.vehicle_type = ?
              AND ps.status = 'AVAILABLE'
              AND ps.id NOT IN (
                  SELECT b.parking_slot_id 
                  FROM bookings b 
                  WHERE b.parking_location_id = ? 
                    AND b.booking_date = ? 
                    AND b.booking_status IN ('PENDING', 'CONFIRMED', 'ACTIVE')
                    AND (
                        (b.start_time <= ? AND b.end_time > ?) OR
                        (b.start_time < ? AND b.end_time >= ?) OR
                        (? <= b.start_time AND ? >= b.end_time)
                    )
              )
        '''
        
        if vehicle_category:
            query += " AND (ps.vehicle_category = ? OR ps.vehicle_category IS NULL OR ps.vehicle_category = '')"
            params = (location_id, vehicle_type, location_id, date, start_time, start_time, end_time, end_time, start_time, end_time, vehicle_category)
        else:
            params = (location_id, vehicle_type, location_id, date, start_time, start_time, end_time, end_time, start_time, end_time)
            
        query += " LIMIT 1"
        slot = db.execute(query, params).fetchone()
        
        if slot:
            cur = db.cursor()
            cur.execute('''
                INSERT INTO bookings (
                    user_id, parking_location_id, parking_slot_id, 
                    booking_date, start_time, end_time, 
                    vehicle_number, vehicle_type, vehicle_category, 
                    booking_status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'PENDING')
            ''', (user_id, location_id, slot['id'], date, start_time, end_time, vehicle_number, vehicle_type, vehicle_category))
            db.commit()
            booking_id = cur.lastrowid
            return redirect(url_for('payment.summary', booking_id=booking_id))
        else:
            flash("No compatible parking slot is available for this time. Please try a different time or location.", "error")
            
    return render_template('user/booking.html', location=location)

@bp.route('/<int:booking_id>/success')
@login_required
def success(booking_id):
    user_id = session.get('user_id')
    booking = Booking.get_booking_by_id(booking_id, user_id)
    
    if not booking or booking['payment_status'] != 'SUCCESS':
        return redirect(url_for('user.dashboard'))
        
    return render_template('user/booking_success.html', booking=booking)

@bp.route('/<int:booking_id>')
@login_required
def details(booking_id):
    user_id = session.get('user_id')
    booking = Booking.get_booking_by_id(booking_id, user_id)
    
    if not booking:
        abort(404)
        
    return render_template('user/booking_details.html', booking=booking)
