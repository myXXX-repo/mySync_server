from flask import Flask

from mySync.apps import init_app
from mySync.config import init_config
from mySync.common.ext import init_ext


def create_server():
    server = Flask(__name__)

    server = init_config(server)

    init_ext(server)  # sql ctrl
    init_app(server)

    return server
