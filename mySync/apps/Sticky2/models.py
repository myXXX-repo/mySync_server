from mySync.common.ext import db


class Sticky2(db.Model):
    # sticky用于存放
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1024))
    con = db.Column(db.String(1024))
    devName = db.Column(db.String(1024))
    time = db.Column(db.String(1024))
    ip = db.Column(db.String(1024))
