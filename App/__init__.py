from flask import Flask

from App.views import init_view

from json import dumps as jsonencode


def create_app():
    app = Flask(__name__)

    init_view(app)

    return app
