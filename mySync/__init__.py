from flask import Flask

from mySync.apps import init_app
# from mySync.apps.Markdown import init_app_Markdown
# from mySync.apps.Sticky import init_app_Sticky
from mySync.config import init_config
from mySync.common.ext import init_ext


def create_server():
    server = Flask(__name__)

    init_config(server)

    init_ext(server)  # sql ctrl
    init_app(server)
    return server
