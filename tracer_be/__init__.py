from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# ---------------------------------
# source venv/bin/activate
# cd tracer_be (from first-level app directory)
# export FLASK_APP=__init__.py && export FLASK_ENV=development
# flask run
# ---------------------------------

db = SQLAlchemy()
login_manager = LoginManager()

# create app
def create_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(24)
    CORS(app)
    # cors = CORS(app, resources={r'/*': {"origins": 'https://tracerscfx.herokuapp.com'}})
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from .auth import auth
        app.register_blueprint(auth.auth_bp)
        from .retrieve import retrieve
        app.register_blueprint(retrieve.retrieve_bp)

        # from . import routes
        db.create_all()

        return app


if __name__ == '__main__':
    app.run(Debug=True)
