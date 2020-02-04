from flask import Blueprint, request, abort
from flask import render_template

from ..models.GitRepoCtrl import GitRepoCtrl

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
    'currrent_commit_id': '',
    'lastUpdateTime': ''
}


def temp():
    repo = GitRepoCtrl(
        'https://github.com/alone-wolf/ifTheDoorOpen.git', locate_path='./data')
    repo.ensureRepoUptodate()


@Git_block.route('/Git_block')
def index():
    th = threading.Thread(target=temp)
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
