from flask_sqlalchemy import SQLAlchemy

from App.ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16))

    def add_save(self):
        db.session.add(self)
        db.session.commit()


class Git(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    repo_name = db.Column(db.String(1024))
    remote_addr = db.Column(db.String(1024))
    local_addr = db.Column(db.String(1024))
    branch = db.Column(db.String(1024))
    last_update_time = db.Column(db.String(1024))
    last_check_time = db.Column(db.String(1024))
    depth = db.Column(db.Integer)
    enabled = db.Column(db.Boolean)

    def add_save(self):
        db.session.add(self)
        db.session.commit()


class Sticky(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(1024))
    con = db.Column(db.String(1024))
    devName = db.Column(db.String(1024))
    ip = db.Column(db.String(1024))

    def add_save(self):
        db.session.add(self)
        db.session.commit()


# class ToDoList(db.Model):
#     def add_save(self):
#         db.session.add(self)
#         db.session.commit()
#
#     pass
#
#
# class Statistic(db.Model):
#     def add_save(self):
#         db.session.add(self)
#         db.session.commit()
#
#     pass


if __name__ == '__main__':
    u = User()
    u.add_save()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(16))
#
#     def add_save(self):
#         db.session.add(self)
#         db.session.commit()
#
#
# class Git(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     repo_name = db.Column(db.String(1024))
#     remote_addr = db.Column(db.String(1024))
#     local_addr = db.Column(db.String(1024))
#     branch = db.Column(db.String(1024))
#     last_update_time = db.Column(db.String(1024))
#     last_check_time = db.Column(db.String(1024))
#     depth = db.Column(db.Integer)
#
#     def add_save(self):
#         db.session.add(self)
#         db.session.commit()
