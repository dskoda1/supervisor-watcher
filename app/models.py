from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from app.database import db
# from app import engine

# Base = declarative_base()

# Set your classes here.

'''
class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
'''
class Supervisors(db.Model):
    __tablename__ = 'Supervisors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    host = db.Column(db.String(40))
    port = db.Column(db.String(5))

    def __init__(self, name=None, host=None, port=None):
        self.name = name
        self.host = host
        self.port = port
