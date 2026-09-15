from utils.database import get_db
from utils.security import hash_password, verify_password

class User:
    @staticmethod
    def create(name, email, phone, password):
        db = get_db()
        try:
            cur = db.cursor()
            cur.execute(
                "INSERT INTO users (name, email, phone, password_hash) VALUES (?, ?, ?, ?)",
                (name, email, phone, hash_password(password))
            )
            db.commit()
            return True, cur.lastrowid
        except db.IntegrityError:
            return False, "Email already exists"

    @staticmethod
    def get_by_email(email):
        db = get_db()
        return db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

    @staticmethod
    def authenticate(email, password):
        user = User.get_by_email(email)
        if user and verify_password(user['password_hash'], password):
            return dict(user)
        return None
