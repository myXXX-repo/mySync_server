from flask import Blueprint
from flask import render_template

config = Blueprint('config', __name__)


@config.route('/config')
def index():
    return render_template('index.html')
