from flask import Blueprint, render_template
from app import db
from app.models import User, Order  # Ensure Order is defined in models.py

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')  # Ensure index.html exists in templates/

@bp.route('/orders')
def orders():
    # Logic to fetch and display orders
    orders = Order.query.all()  # Assuming Order model has been defined
    return render_template('order_management.html', orders=orders)  # Pass orders to template

