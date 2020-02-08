from mySync.common.ext import db


class Sticky(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1024))
    con = db.Column(db.String(1024))
    devName = db.Column(db.String(1024))
    ip = db.Column(db.String(1024))

    def add_save(self):
        db.session.add(self)
        db.session.commit()