import requests
import jwt
import datetime
from flask import current_app, jsonify, request
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import stripe

# Initialize Stripe
stripe.api_key = current_app.config.get('STRIPE_SECRET_KEY')

def generate_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            current_app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_token(token):
    """
    Decodes the auth token
    :param token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = decode_token(token)
            current_user = data['sub']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

def hash_password(password):
    return generate_password_hash(password)

def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def process_stripe_payment(amount, currency='usd', source=None, description=''):
    """
    Process payment via Stripe
    """
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Stripe charges in cents
            currency=currency,
            source=source,
            description=description
        )
        return charge
    except stripe.error.StripeError as e:
        return {'error': str(e)}

def process_airtel_payment(phone_number, amount, currency='SLL'):
    """
    Process payment via Airtel Money
    """
    url = 'https://api.airtel.com/payment'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {current_app.config.get("AIRTEL_MONEY_API_KEY")}'
    }
    data = {
        'phoneNumber': phone_number,
        'amount': amount,
        'currency': currency
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def process_paypal_payment(amount, currency='USD'):
    """
    Process payment via PayPal
    """
    url = 'https://api-m.sandbox.paypal.com/v1/payments/payment'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {get_paypal_token()}'
    }
    data = {
        'intent': 'sale',
        'payer': {
            'payment_method': 'paypal'
        },
        'transactions': [{
            'amount': {
                'total': amount,
                'currency': currency
            },
            'description': 'Payment description'
        }],
        'redirect_urls': {
            'return_url': 'http://localhost:5000/payment/success',
            'cancel_url': 'http://localhost:5000/payment/cancel'
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_paypal_token():
    """
    Get PayPal OAuth Token
    """
    url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'
    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en_US'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, headers=headers, data=data, auth=(current_app.config.get('PAYPAL_CLIENT_ID'), current_app.config.get('PAYPAL_CLIENT_SECRET')))
    return response.json().get('access_token')

def process_bank_payment(account_number, amount, currency='SLL'):
    """
    Process payment via Bank
    """
    url = 'https://api.bank.com/transactions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {current_app.config.get("BANK_API_KEY")}'
    }
    data = {
        'accountNumber': account_number,
        'amount': amount,
        'currency': currency
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
