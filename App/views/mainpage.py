from flask import Blueprint
from flask import render_template

from App.models import db
from App.models import User

mainpage = Blueprint('mainpage', __name__)


@mainpage.route('/')
def index():
    return render_template('index.html', title1='mySync', title2='index')


@mainpage.route('/mainpage')
def mmm():
    return render_template('m.html')


@mainpage.route('/createdb')
def createdb():
    print('init db ...')
    db.create_all()
    return '21'

@mainpage.route('/dropdb')
def dropdb():
    db.drop_all()
    return 'delete succeed'

@mainpage.route('/adduser')
def adduser():
    user = User()
    user.username = 'aaa'

    user.save()
    return '22'
