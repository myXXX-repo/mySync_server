from mySync.common.ext import db


class Statistics(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_name = db.Column(db.String(100))
    route = db.Column(db.String(1024))
    call_date = db.Column(db.String(1024))
    ip = db.Column(db.String(1024))
    devName = db.Column(db.String(1024))

    def add_save(self):
        db.session.add(self)
        db.session.commit()


def db_insert(app_name, route, call_date, ip, devName):
    statistics = Statistics()
    statistics.app_name = app_name
    statistics.route = route
    statistics.call_date = call_date
    statistics.ip = ip
    statistics.devName = devName
