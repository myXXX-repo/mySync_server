from mySync.apps.VisitCounter.routes import VisitCounter_routes


def init_app_VisitCounter(server):
    server.register_blueprint(VisitCounter_routes)
    return server
