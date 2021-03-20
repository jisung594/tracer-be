import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'sqlite3.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    API_KEY = os.environ.get('FINNHUB_API_KEY')
