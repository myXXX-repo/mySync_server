from mySync.apps.ApplicationData.routes import ApplicationData_routes


def init_app_ApplicationData(server):
    server.register_blueprint(ApplicationData_routes)
    return server
