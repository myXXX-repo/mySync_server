from mySync.common.ext import db


class VisitCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    route = db.Column(db.String(1024))
    time = db.Column(db.String(1024))
    ip = db.Column(db.String(1024))

    def add_save(self):
        db.session.add(self)
        db.session.commit()


def db_insert(route, time, ip):
    visitcounter = VisitCounter()
    visitcounter.route = route
    visitcounter.time = time
    visitcounter.ip = ip
    visitcounter.add_save()


def db_show(limit=0):
    visitCounter = VisitCounter()
    if limit != 0:
        pass
    pass
