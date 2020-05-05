from flask_restful import Api, Resource
from flask import Blueprint, request, abort, jsonify

from mySync.apps.Git.libs import GitRepoCtrl

import threading

from mySync.apps.Git.models import add_ones, Git, get_all, del_all
from mySync.common.access_token_check import check_access_token

from mySync.common.libs import jsonEncode
from mySync.common.libs import jsonDecode


def db_rec2list(rec2):
    repo_list = []
    for i in rec2:
        a = {
            "id": i.id,
            "repo_name": i.repo_name,
            "remote_addr": i.remote_addr,
            "local_addr": i.local_addr,
            "branch": i.branch,
            "depth": i.depth
        }
        repo_list.append(a)
    return repo_list


def handle_repo(git_repos):
    for i in git_repos:
        if i.enabled == 'disabled':
            print('repo {} disabled, but still exists for future using'.format(i.repo_name))
            continue
        repo = GitRepoCtrl(i.remote_addr, i.local_addr)
        repo.ensureRepoUptodate()
    print('repo update done')


class Git_repos(Resource):
    @staticmethod
    @check_access_token
    def get():
        return jsonify(db_rec2list(get_all()))

    @staticmethod
    @check_access_token
    def post():
        request_data = request.args.to_dict()
        print(request_data)

        if len(request_data) != len(set(request_data)):
            print("got repeated keys")
            return abort(400)

        keys = ['repo_name', 'remote_addr', 'local_addr', 'branch', 'depth']
        for key in keys:
            if key not in request_data:
                print("got missing key(s)")
                return abort(400)
            if request_data[key] == "":
                print("got missing value(s)")
                return abort(400)

        gits = [i.remote_addr for i in get_all()]
        if request_data['remote_addr'] in gits:
            print("repo exists, skipping")
            return "repo exists, skipping"

        newGit = Git(repo_name=request_data['repo_name'],
                     remote_addr=request_data['remote_addr'],
                     local_addr=request_data['local_addr'],
                     branch=request_data['branch'],
                     depth=request_data['depth'],
                     enabled=True)

        add_ones([newGit])

        return 'add done'

    @staticmethod
    @check_access_token
    def delete():
        del_all()
        return "del git repos done"


Git_routes = Blueprint('Git_routes', __name__)

Git_api = Api(Git_routes)

Git_api.add_resource(Git_repos, '/app/Git')


@Git_routes.route('/app/Git/ensureuptodate', methods=['GET'])
@check_access_token
def ensure():
    len(get_all())
    th = threading.Thread(target=handle_repo, args=(get_all(),))
    th.start()
    return 'cmd running'


@Git_routes.route('/app/Git/test', methods=['GET'])
@check_access_token
def test_server():
    return "server is fine"

# git 增 删全部 查
