from flask import Blueprint, request, abort
from flask import render_template

from mySync.common.ext import db

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/')
def index():
    return render_template('index.html', title1='mySync', title2='index')


@main_routes.route('/persent')
def persent():
    return render_template('persent.html', title1='mySync', title2='persent')


@main_routes.route('/getip')
def config_getip():
    return request.remote_addr


@main_routes.route('/createdb')
def createdb():
    db.create_all()
    return 'db created'


@main_routes.route('/dropdb')
def dropdb():
    db.drop_all()
    return 'drop down'


@main_routes.route('/test/errorpage/<int:errcode>')
def test_error_page(errcode):
    return abort(errcode)


@main_routes.route('/test/request')
def test_request():
    return render_template("test_request.html", title1="mySync", title2="testrequest")

