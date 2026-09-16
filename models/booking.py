from utils.database import get_db

class Booking:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    @staticmethod
    def get_upcoming_for_user(user_id):
        db = get_db()
        return db.execute('''
            SELECT b.*, pl.name as parking_name, pl.address as parking_address, ps.slot_number 
            FROM bookings b
            JOIN parking_locations pl ON b.parking_location_id = pl.id
            JOIN parking_slots ps ON b.parking_slot_id = ps.id
            WHERE b.user_id = ? AND b.booking_status IN ('CONFIRMED', 'ACTIVE')
            ORDER BY b.booking_date ASC, b.start_time ASC
            LIMIT 1
        ''', (user_id,)).fetchone()

    @staticmethod
    def get_booking_by_id(booking_id, user_id):
        db = get_db()
        return db.execute('''
            SELECT b.*, pl.name as parking_name, pl.address as parking_address, ps.slot_number 
            FROM bookings b
            JOIN parking_locations pl ON b.parking_location_id = pl.id
            JOIN parking_slots ps ON b.parking_slot_id = ps.id
            WHERE b.id = ? AND b.user_id = ?
        ''', (booking_id, user_id)).fetchone()

    @staticmethod
    def update_status(booking_id, booking_status, payment_status, qr_token=None):
        db = get_db()
        cur = db.cursor()
        cur.execute('''
            UPDATE bookings 
            SET booking_status = ?, payment_status = ?, qr_token = COALESCE(?, qr_token)
            WHERE id = ?
        ''', (booking_status, payment_status, qr_token, booking_id))
        db.commit()

    @staticmethod
    def get_all_for_user(user_id):
        db = get_db()
        return db.execute('''
            SELECT b.*, pl.name as parking_name, pl.address as parking_address, ps.slot_number 
            FROM bookings b
            JOIN parking_locations pl ON b.parking_location_id = pl.id
            JOIN parking_slots ps ON b.parking_slot_id = ps.id
            WHERE b.user_id = ?
            ORDER BY b.booking_date DESC, b.start_time DESC
        ''', (user_id,)).fetchall()
