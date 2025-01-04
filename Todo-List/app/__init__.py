from flask import Flask, render_template
from .config import Config
from .models import db
from .routes import api

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize database
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(api, url_prefix='/api')
    
    # Add main route
    @app.route('/')
    def index():
        return render_template('index.html')
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app