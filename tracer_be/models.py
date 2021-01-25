from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), index=True, unique=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.email)


# *** flask shell ***
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///sqlite3.db')
# from tracer_be.models import User
# j = User(email='jisung594@gmail.com', first_name='Jon', last_name='Choi', password='password')

# from tracer_be.__init__ import db
# from flask import Flask
# app = Flask(__name__)
# db.init_app(app)
# from tracer_be.models import User
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///sqlite3.db')
# jon = User(email='jisung594@gmail.com', first_name='Jon', last_name='Choi', password='password')
# db.create_all()
# db.session.add(jon)
# db.session.commit()
