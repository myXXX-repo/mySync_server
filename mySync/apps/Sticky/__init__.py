from mySync.apps.Sticky.routes import Sticky_routes


def init_app_Sticky(server):
    server.register_blueprint(Sticky_routes)
    return server
