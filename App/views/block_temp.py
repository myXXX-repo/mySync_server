from flask import Blueprint, request
from flask import render_template

# from json import dumps as jsonencode

block_temp = Blueprint('block_temp', __name__)


@block_temp.route('/config')
def index():
    return render_template('index.html')


@block_temp.route('/config/getip')
def config_getip():
    return request.remote_addr
