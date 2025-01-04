import pytest
from app import create_app
from app.models import db
from app.config import Config
import os

class TestConfig(Config):
    TESTING = True
    # Use environment variable or fallback to SQLite for testing
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'TEST_DATABASE_URL',
        'sqlite:///:memory:'  # Use in-memory SQLite by default
    )
    # Disable CSRF protection in testing
    WTF_CSRF_ENABLED = False

@pytest.fixture(scope='function')
def app():
    """Create and configure a new app instance for each test."""
    # Create the app with test config
    app = create_app(TestConfig)
    
    # Create a test context
    with app.app_context():
        # Create all tables
        db.create_all()
        yield app
        # Clean up after the test
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    """Create a test client for the app."""
    return app.test_client()

@pytest.fixture(scope='function')
def runner(app):
    """Create a test runner for CLI commands."""
    return app.test_cli_runner()