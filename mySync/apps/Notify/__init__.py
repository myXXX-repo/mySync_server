from flask import Blueprint

from mySync.apps.Notify.routes import Notify_routes


def init_app_Notify(server):
    server.register_blueprint(Notify_routes)
    return server
