import unittest
from app import create_app
from flask import session
from utils.database import get_db
import sqlite3
import os

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        with self.app.app_context():
            db = get_db()
            db.execute("DELETE FROM users WHERE email='newuser@smartpark.local'")
            db.commit()

    def test_registration(self):
        response = self.client.post('/auth/register', data=dict(
            name='New User',
            email='newuser@smartpark.local',
            phone='9876543210',
            password='password123',
            confirm_password='password123',
            terms='on'
        ))
        self.assertEqual(response.status_code, 302) # Redirect to login

    def test_login_success(self):
        # We assume user@smartpark.local exists with 'user123' from seed.py
        with self.client as c:
            response = c.post('/auth/login', data=dict(
                email='user@smartpark.local',
                password='user123'
            ))
            self.assertEqual(response.status_code, 302)
            self.assertIn('user_id', session)
        
    def test_login_invalid_password(self):
        with self.client as c:
            response = c.post('/auth/login', data=dict(
                email='user@smartpark.local',
                password='wrongpassword'
            ))
            self.assertEqual(response.status_code, 200) # Re-render login
            self.assertNotIn('user_id', session)

    def test_admin_login(self):
        with self.client as c:
            response = c.post('/admin/login', data=dict(
                email='admin@smartpark.local',
                password='admin123'
            ))
            self.assertEqual(response.status_code, 302)
            self.assertIn('admin_id', session)

    def test_unauthorized_access(self):
        response = self.client.get('/user/dashboard')
        self.assertEqual(response.status_code, 302) # Redirect to login

    def test_logout(self):
        with self.client as c:
            c.post('/auth/login', data=dict(
                email='user@smartpark.local',
                password='user123'
            ))
            response = c.get('/auth/logout')
            self.assertEqual(response.status_code, 302)
            self.assertNotIn('user_id', session)

    def test_unauthorized_routes(self):
        protected_routes = ['/booking/', '/parking/', '/payment/', '/prediction/', '/qr/', '/otp/']
        for route in protected_routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 302, f"Route {route} did not redirect.")
            
    def test_admin_route_unauthorized(self):
        # A normal user attempting admin access
        with self.client as c:
            c.post('/auth/login', data=dict(
                email='user@smartpark.local',
                password='user123'
            ))
            response = c.get('/admin/dashboard')
            self.assertEqual(response.status_code, 302) # Redirects to admin login because of admin_required

class CSRFTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = True
        self.client = self.app.test_client()

    def test_missing_csrf_token(self):
        response = self.client.post('/auth/login', data=dict(
            email='user@smartpark.local',
            password='user123'
        ))
        # Flask-WTF CSRFProtect returns 400 Bad Request on missing token
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
