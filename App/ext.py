from flask_sqlalchemy import SQLAlchemy
# from json import dumps as jsonencode
# from json import loads as jsondecode
# import os

db = SQLAlchemy()


def init_ext(app):
    db.init_app(app)


