import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def init_db():
    print(f"Initializing database at {DB_PATH}")
    with sqlite3.connect(DB_PATH) as conn:
        with open(SCHEMA_PATH, 'r') as f:
            conn.executescript(f.read())
        
        conn.execute('''
            INSERT INTO admins (name, email, password_hash) 
            VALUES ('Admin User', 'admin@smartpark.local', 'scrypt:32768:8:1$guL3NAO9rarc5lzF$82de66913adaea15d45c50083ae6759538f81522ddc40adeffd7f33649b95ed1906ce688ddf574189df6fc5ada928c6807160608fa80919b17b8cdb64ee28e7d')
        ''')
        
        conn.execute('''
            INSERT INTO users (name, email, phone, password_hash, is_verified) 
            VALUES ('Test User', 'user@smartpark.local', '1234567890', 'scrypt:32768:8:1$nO0niFE8oqVwpmOA$84fbdcf3912b5ecb88492ad33ec931eb1ef0aa5c076a579994effb10ae84e64866ce3018ceaea8e7338d5fe852a2dc2c96998ded2046b77860bbf08322bcc096', 1)
        ''')
        
        conn.commit()
    print("Database initialized and seeded successfully.")

if __name__ == '__main__':
    init_db()
