from utils.database import get_db

class Notification:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
            
    @staticmethod
    def get_recent_for_user(user_id, limit=3):
        db = get_db()
        return db.execute('''
            SELECT * FROM notifications 
            WHERE user_id = ? 
            ORDER BY created_at DESC 
            LIMIT ?
        ''', (user_id, limit)).fetchall()
