from flask_sqlalchemy import SQLAlchemy

from App.ext import db


# class model(db.Model):
#     pass


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))

    def save(self):
        db.session.add(self)
        db.session.commit()
