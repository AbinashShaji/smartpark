import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'smartpark-secret-key'
    DATABASE_PATH = os.environ.get('DATABASE_PATH') or os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database', 'database.db')
    
    # Session Security Hardening
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    # Use Secure cookies only in production to allow local HTTP testing
    SESSION_COOKIE_SECURE = os.environ.get('FLASK_ENV') == 'production'
