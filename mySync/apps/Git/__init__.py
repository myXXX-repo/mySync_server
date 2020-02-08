from mySync.apps.Git.routes import Git_routes


def init_app_Git(server):
    server.register_blueprint(Git_routes)
    return server
