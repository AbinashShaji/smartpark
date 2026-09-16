import os
from flask import Flask, render_template
from config import Config
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app(config_class=Config):
    # Configure template and static folders
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    app.config.from_object(config_class)

    # Initialize CSRF protection
    csrf.init_app(app)

    # Initialize database connection context
    from utils import database
    database.init_app(app)

    # Register Blueprints
    from routes.public import bp as public_bp
    app.register_blueprint(public_bp)

    from routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from routes.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from routes.admin import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from routes.parking import bp as parking_bp
    app.register_blueprint(parking_bp, url_prefix='/parking')

    from routes.booking import bp as booking_bp
    app.register_blueprint(booking_bp, url_prefix='/booking')

    from routes.payment import bp as payment_bp
    app.register_blueprint(payment_bp, url_prefix='/payment')

    from routes.prediction import bp as prediction_bp
    app.register_blueprint(prediction_bp, url_prefix='/prediction')

    from routes.qr import bp as qr_bp
    app.register_blueprint(qr_bp, url_prefix='/qr')

    from routes.otp import bp as otp_bp
    app.register_blueprint(otp_bp, url_prefix='/otp')

    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('public/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('public/500.html'), 500

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
