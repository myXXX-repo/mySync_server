from mySync.common.ext import db


class temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
