from flask import Blueprint
from flask import render_template

mainpage = Blueprint('mainpage', __name__)


@mainpage.route('/')
def index():
    return render_template('index.html', title1='mySync', title2='index')

@mainpage.route('/mainpage')
def mmm():
    return render_template('m.html')
