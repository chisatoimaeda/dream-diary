import os

basedir = os.path.dirname(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'timeline.sqlite')
SECRET_KEY = os.urandom(10)
