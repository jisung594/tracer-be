from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# ---------------------------------
# source venv/bin/activate
# export FLASK_APP=__init__.py && export FLASK_ENV=development
# flask run
# ---------------------------------

db = SQLAlchemy()

# create app
def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)
    app.config.from_object('config.Config')
    # migrate = Migrate(app, db)

    db.init_app(app)

    with app.app_context():
        # from . import routes
        db.create_all()

        return app
