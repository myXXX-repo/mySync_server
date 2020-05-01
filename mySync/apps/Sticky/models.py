from mySync.common.ext import db


class Sticky(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1024))
    con = db.Column(db.String(1024))
    dev_name = db.Column(db.String(1024))
    time = db.Column(db.String(1024))
    ip = db.Column(db.String(1024))

    # def add_save(self):
    #     db.session.add(self)
    #     db.session.commit()
    #
    # # def getAll(self):
    # #     return


def db_insert(title, con, time, dev_name, ip):
    sticky = Sticky()
    sticky.title = title
    sticky.con = con
    sticky.time = time
    sticky.dev_name = dev_name
    sticky.ip = ip
    # sticky.add_save()

    db.session.add(sticky)
    db.session.commit()


def add_one(sticky):
    db.session.add(sticky)
    db.session.commit()


def add_ones(stickies=None):
    if stickies is None:
        stickies = []
    for i in stickies:
        db.session.add(i)
    db.session.commit()





def getAll():
    sticky = Sticky()
    result = sticky.query.all()
    print(result.id)
    return result
