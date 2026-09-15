from utils.database import get_db
from utils.security import verify_password

class Admin:
    @staticmethod
    def get_by_email(email):
        db = get_db()
        return db.execute("SELECT * FROM admins WHERE email = ?", (email,)).fetchone()

    @staticmethod
    def authenticate(email, password):
        admin = Admin.get_by_email(email)
        if admin and verify_password(admin['password_hash'], password):
            return dict(admin)
        return None
