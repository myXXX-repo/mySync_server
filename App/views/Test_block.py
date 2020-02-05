from flask import Blueprint, request, abort
from flask import render_template
# from ..ext import DataArray
# from json import dumps as jsonencode

Test_block = Blueprint('Test_block', __name__)


@Test_block.route('/test/errorpage/<int:errcode>')
def test_error_page(errcode):
    return abort(errcode)


@Test_block.route('/test/request')
def test_request():
    return render_template("test_request.html", title1="mySync", title2="testrequest")
