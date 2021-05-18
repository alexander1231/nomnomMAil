import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    DEBUG = True
    # SQLALCHEMY_DATBASE_URI = os.environ.get('DATABASE_URL') or 'mysql+mysqlconnector://galizacademy:p6n2w4wiev1w62wg@db-mysql-nyc1-galiz-do-user-8296012-0.b.db.ondigitalocean.com:25060/galizacademy'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+mysqlconnector://root:root@127.0.0.1:6603/nomnomdata'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

