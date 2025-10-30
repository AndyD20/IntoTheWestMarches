from flask import Flask
from .extensions import db
from .markers import bp as markers_bp
from flask_cors import CORS

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    CORS(app)

    with app.app_context():
        # Register Blueprints
        app.register_blueprint(markers_bp, url_prefix='/markers')

        db.create_all()

        return app