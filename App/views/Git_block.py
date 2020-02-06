from flask import Blueprint, request, abort

from ..ext import DataArray
from App.ext.GitRepoCtrl import GitRepoCtrl

import threading

# from json import dumps as jsonencode

Git_block = Blueprint('Git_block', __name__)

dataPath = 'data/'

gitlistfilename = 'Gitlist.json'

gitlist_node = {
    'reponame': '',
    'remote_addr': '',
    'local_addr': '',
    'branch': '',
    'current_commit_id': '',
    'lastUpdateTime': '',
}

gitrepolist = DataArray('data/GitRepos.json')


def handle_repo():
    gitlist = [
        {
            'remote_addr': 'https://github.com/alone-wolf/ifTheDoorOpen.git',
            'local_addr': './data'
        },
        {
            'remote_addr': 'https://github.com/alone-wolf/learn_doc_md.git',
            'local_addr': './data'
        }
    ]
    for i in gitlist:
        repo = GitRepoCtrl(i['remote_addr'], i['local_addr'])
        repo.ensureRepoUptodate()
    print('repo update done')


@Git_block.route('/Git/ensureuptodate')
def index():
    th = threading.Thread(target=handle_repo)
    th.start()
    return 'cmd recived'


@Git_block.route('/v<float:version>/Git', methods=['GET', 'POST', 'DELETE'])
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


@Git_block.route('/v<float:version>/Git/<reponame>', methods=['GET', 'POST', 'DELETE'])
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
