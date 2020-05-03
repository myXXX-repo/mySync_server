from flask import Blueprint
from flask import request
from flask import abort
from functools import wraps
from flask import redirect
from flask import url_for
from flask import render_template

from mySync.apps.Markdown.routes import Markdown_routes
from mySync.common.access_token_check import check_access_token
from mySync.common.ext import db
from mySync.config.settings import settings
from hmac import compare_digest

main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/')
def index():
    db.create_all()
    return render_template('index.html', title1='mySync', title2='index', per=20)


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


@main_routes.route('/test/token')
@check_access_token
def test_token():
    return "access token checked"
