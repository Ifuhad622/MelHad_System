from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import yaml
import os

db = SQLAlchemy()
migrate = Migrate()

def load_config():
    # Update the path to the config.yaml file
    config_path = os.path.join(os.path.dirname(__file__), '../config/config.yaml')
    if not os.path.exists(config_path):
        raise Exception(f"Config file not found at {config_path}")
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)

def create_app():
    app = Flask(__name__)

    # Load the configuration
    config = load_config()
    app.config.from_mapping(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import bp as main_bp  # Ensure this import is correct
    app.register_blueprint(main_bp)  # Register the blueprint

    return app

