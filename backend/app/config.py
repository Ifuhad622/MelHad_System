import os
from pathlib import Path
import yaml

BASE_DIR = Path(__file__).resolve().parent

class Config:
    # Load configuration from config.yaml
    with open(BASE_DIR / 'config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)

    # Load from environment variables or fallback to config.yaml
    SECRET_KEY = os.getenv('SECRET_KEY', config.get('SECRET_KEY', 'a5d89654e803cb65eaf29dcc44b65893'))
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', config.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', config.get('SQLALCHEMY_TRACK_MODIFICATIONS', False))

    # Stripe settings
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', config.get('STRIPE_PUBLIC_KEY', 'pk_test_51OiImeAcBZ0vmFyCUiOpNYupFpilMViAqQrjj3KzeEPMlcvcw77oLj91xbynAu8Kzh06OCjuHCos7G9k0CFmwz4Z00SsOUqMuJ'))
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', config.get('STRIPE_SECRET_KEY', 'sk_test_51OiImeAcBZ0vmFyCIAaxOuYvCwrwuDP9KgCUwKbiMGINxJYGFpOHXF3RM8wq122DujLBkTg92x1vN25nvgLXSULS00XE6VWtE3'))

    # Twilio settings
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', config.get('TWILIO_ACCOUNT_SID', 'AC61720f15666d613b344a2ae9c5c7bc6e'))
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', config.get('TWILIO_AUTH_TOKEN', '5024f8ba078b85b393294b62b137415b'))
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER', config.get('TWILIO_PHONE_NUMBER', 'your_twilio_phone_number'))

    # Airtel Money settings
    AIRTEL_MONEY_API_KEY = os.getenv('AIRTEL_MONEY_API_KEY', config.get('AIRTEL_MONEY_API_KEY', 'your_airtel_money_api_key'))
    AIRTEL_MONEY_SECRET_KEY = os.getenv('AIRTEL_MONEY_SECRET_KEY', config.get('AIRTEL_MONEY_SECRET_KEY', 'your_airtel_money_secret_key'))

    # PayPal settings
    PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID', config.get('PAYPAL_CLIENT_ID', 'AcZw00B3hUZSPgI7Cf6XTYJEsq85njx4VoW65XbLI5HalgZpigrlFu-QFVl6zGrKpPiIe3LvnCbnVJ5U'))
    PAYPAL_CLIENT_SECRET = os.getenv('PAYPAL_CLIENT_SECRET', config.get('PAYPAL_CLIENT_SECRET', 'EI94BbUDGbpM6Kti7ihVE_g-FOAVENL6b6lfUpJIELisNmpzRUmNMawZO81Wz0YUPtCJEVRQwQIi6Mpl'))

    # Bank settings
    BANK_API_KEY = os.getenv('BANK_API_KEY', config.get('BANK_API_KEY', 'your_bank_api_key'))
    BANK_API_SECRET = os.getenv('BANK_API_SECRET', config.get('BANK_API_SECRET', 'your_bank_api_secret'))

    # Other settings
    DEBUG = os.getenv('DEBUG', config.get('DEBUG', True)) == 'True'
    MAIL_SERVER = os.getenv('MAIL_SERVER', config.get('MAIL_SERVER', 'smtp.googlemail.com'))
    MAIL_PORT = os.getenv('MAIL_PORT', config.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', config.get('MAIL_USE_TLS', True)) == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', config.get('MAIL_USERNAME', 'melhad0121@gmail.com'))
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', config.get('MAIL_PASSWORD', 'Fuhad@001'))
    ADMINS = os.getenv('ADMINS', ','.join(config.get('ADMINS', ['melhad0121@gmail.com']))).split(',')

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
    'production': ProductionConfig,
}

