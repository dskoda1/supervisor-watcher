from flask import Flask, request as req
from flask_sqlalchemy import SQLAlchemy
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, create_session
from config.development import SQLALCHEMY_DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base

engine = None
db_session = scoped_session(lambda: create_session(bind=engine))

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.logger.setLevel(logging.NOTSET)

    from app.controllers import pages
    app.register_blueprint(pages.blueprint)

    app.engine = init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    from app.database import db

    db.init_app(app)
    # Base.metadata.create_all(bind=engine)



    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    return app

def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    return engine
