from mySync.apps.Git import Git_routes
from mySync.apps.Main import main_routes
from mySync.apps.Markdown import Markdown_routes
from mySync.apps.Sticky import Sticky_routes


def init_app(server):
    server.register_blueprint(main_routes)
    server.register_blueprint(Sticky_routes)
    server.register_blueprint(Markdown_routes)
    server.register_blueprint(Git_routes)
    return server
