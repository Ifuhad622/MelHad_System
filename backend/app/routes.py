from flask import Blueprint, render_template, request
from app import db
from app.models import User, Order

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/orders')
def orders():
    # Logic to fetch and display orders
    return render_template('order_management.html')
