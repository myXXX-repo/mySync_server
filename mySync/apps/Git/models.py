import time

from mySync.common.ext import db

get_now_milli_time = lambda: int(time.time() * 1000)


class Git(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repo_name = db.Column(db.String(1024))
    remote_addr = db.Column(db.String(1024))
    local_addr = db.Column(db.String(1024))
    branch = db.Column(db.String(1024))
    create_time = db.Column(db.String(100), default=get_now_milli_time)
    last_update_time = db.Column(db.String(1024))
    last_check_time = db.Column(db.String(1024))
    depth = db.Column(db.Integer)
    enabled = db.Column(db.Boolean)


def add_ones(gits=None):
    if gits is None:
        gits = []
    for i in gits:
        db.session.add(i)
    db.session.commit()


def del_one_by_repo_name(repo_name):
    try:
        Git.query.filter(Git.repo_name == repo_name).delete()
    except:
        db.session.rollback()
    finally:
        db.session.commit()


def del_all():
    try:
        db.session.query(Git).delete()
    except:
        db.session.rollback()
    finally:
        db.session.commit()


def get_all():
    return Git.query.all()
