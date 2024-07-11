import os
from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent

class Config:
    # Load configuration from config.yaml
    with open(BASE_DIR / 'config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    SECRET_KEY = config.get('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = config.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    
    # Stripe settings
    STRIPE_PUBLIC_KEY = config.get('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = config.get('STRIPE_SECRET_KEY', '')
    
    # Twilio settings
    TWILIO_ACCOUNT_SID = config.get('TWILIO_ACCOUNT_SID', '')
    TWILIO_AUTH_TOKEN = config.get('TWILIO_AUTH_TOKEN', '')
    TWILIO_PHONE_NUMBER = config.get('TWILIO_PHONE_NUMBER', '')

    # Airtel Money settings
    AIRTEL_MONEY_API_KEY = config.get('AIRTEL_MONEY_API_KEY', '')
    AIRTEL_MONEY_SECRET_KEY = config.get('AIRTEL_MONEY_SECRET_KEY', '')

    # PayPal settings
    PAYPAL_CLIENT_ID = config.get('PAYPAL_CLIENT_ID', '')
    PAYPAL_CLIENT_SECRET = config.get('PAYPAL_CLIENT_SECRET', '')

    # Bank settings
    BANK_API_KEY = config.get('BANK_API_KEY', '')
    BANK_API_SECRET = config.get('BANK_API_SECRET', '')

    # Other settings
    DEBUG = config.get('DEBUG', True)
    MAIL_SERVER = config.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = config.get('MAIL_PORT', 587)
    MAIL_USE_TLS = config.get('MAIL_USE_TLS', True)
    MAIL_USERNAME = config.get('MAIL_USERNAME', '')
    MAIL_PASSWORD = config.get('MAIL_PASSWORD', '')
    ADMINS = config.get('ADMINS', ['your-email@example.com'])

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
