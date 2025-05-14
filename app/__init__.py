from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprint and error issues
    from .views import bp as main_bp
    app.register_blueprint(main_bp)

    from .errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    return app
