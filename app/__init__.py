import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'cast.sqlite'),
            SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(app.instance_path,
                'cast.sqlite'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    # Load from default config if a test config is not specified
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # Ensure the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Set view to send unauthorized users
    login.login_view = 'auth.login'

    # Initialize SQLAlchemy and flask-login
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    # Register our blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app
