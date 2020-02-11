from mySync.common.ext import db


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


def db_insert(repo_name, remote_addr, local_addr, branch, depth):
    git = Git()
    git.repo_name = repo_name
    git.remote_addr = remote_addr
    git.local_addr = local_addr
    git.branch = branch
    git.depth = depth
    git.add_save()
