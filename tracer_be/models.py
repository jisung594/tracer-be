from tracer_be import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), index=True, unique=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def serialize(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return '<User {}>'.format(self.email)



# *** flask shell ***
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///sqlite3.db')
# from tracer_be.models import User
# j = User(email='jisung594@gmail.com', first_name='Jon', last_name='Choi', password='password')

# from tracer_be import db
# db.engine.table_names()
# db.engine.execute('select * from users').fetchall()
