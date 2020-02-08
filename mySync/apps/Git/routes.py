from flask import Blueprint, request, abort

from mySync.apps.Git.libs import GitRepoCtrl

import threading

# from json import dumps as jsonencode
from mySync.apps.Git.models import Git

Git_routes = Blueprint('Git_routes', __name__)

dataPath = 'data/'

gitlistfilename = 'Gitlist.json'

gitlist_node = {
    'reponame': '',
    'remote_addr': '',
    'local_addr': '',
    'branch': '',
    'lastUpdateTime': '',
}

# gitrepolist = DataArray('data/GitRepos.json')


def handle_repo():
    gitlist = [
        {
            'status': 'disabled',
            'repo_name': 'ifTheDoorOpen',
            'remote_addr': 'https://github.com/alone-wolf/ifTheDoorOpen.git',
            'local_addr': './data',
            'branch': 'master',
            'last_update_time': '',
            'last_check_time': ''
        },
        {
            'status': 'enabled',
            'repo_name': 'learn_doc_md',
            'remote_addr': 'https://github.com/alone-wolf/learn_doc_md.git',
            'local_addr': './data',
            'branch': 'master',
            'last_update_time': '',
            'last_check_time': ''
        }
    ]
    for i in gitlist:
        if i['status'] == 'disabled':
            print('repo {} disabled, but still exists for using'.format(i['repo_name']))
            continue
        repo = GitRepoCtrl(i['remote_addr'], i['local_addr'])
        repo.ensureRepoUptodate()
    print('repo update done')


@Git_routes.route('/Git/ensureuptodate')
def index():
    th = threading.Thread(target=handle_repo)
    th.start()
    return 'cmd recived'


@Git_routes.route('/v<float:version>/Git', methods=['GET', 'POST', 'DELETE'])
def gitCtrl(version):
    if version == 1.0:
        return abort(404)
    elif version == 2.0:
        return abort(404)

    elif version == 2.1:
        access_method = request.method

        if access_method == 'GET':
            pass
        elif access_method == 'POST':
            pass
        elif access_method == 'DELETE':
            pass
        else:
            return abort(405)
    else:
        return abort(404)


@Git_routes.route('/v<float:version>/Git/<reponame>', methods=['GET', 'POST', 'DELETE'])
def gitrepoCtrl(version, reponame):
    if version == 1.0:
        return abort(404)
    elif version == 2.0:
        return abort(404)

    elif version == 2.1:
        access_method = request.method

        if access_method == 'GET':
            pass
        elif access_method == 'POST':
            pass
        elif access_method == 'DELETE':
            pass
        else:
            return abort(405)
    else:
        return abort(404)


# test
@Git_routes.route('/Git/addgit')
def test():
    gitrepo = Git()
    gitrepo.repo_name = 'aaa'
    gitrepo.add_save()
    return 'add done'
