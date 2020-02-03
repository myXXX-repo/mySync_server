from flask import Blueprint, request
from flask import render_template
# from json import dumps as jsonencode

Config_block = Blueprint('Config_block', __name__)


@Config_block.route('/config')
def index():
    return render_template('index.html')


@Config_block.route('/config/getip')
def config_getip():
    return request.remote_addr

