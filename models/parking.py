from utils.database import get_db

class Parking:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    @staticmethod
    def get_all_locations():
        db = get_db()
        return db.execute('''
            SELECT * FROM parking_locations 
            WHERE status = 'ACTIVE'
            ORDER BY name ASC
        ''').fetchall()

    @staticmethod
    def get_location_by_id(location_id):
        db = get_db()
        return db.execute('''
            SELECT * FROM parking_locations 
            WHERE id = ? AND status = 'ACTIVE'
        ''', (location_id,)).fetchone()
