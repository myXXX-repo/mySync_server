from flask import Blueprint, request
from flask import render_template

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


@Git_block.route('/Git_block')
def index():
    return render_template('index.html')
