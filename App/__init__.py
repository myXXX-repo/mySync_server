from flask import Flask

from App.ext import init_ext
from App.settings import init_setting
from App.views import init_view


def create_app():
    app = Flask(__name__)

    init_setting(app)
    init_ext(app)
    init_view(app)
    return app
