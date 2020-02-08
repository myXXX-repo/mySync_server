from mySync.apps.Main.routes import main_routes

def init_app_Main(server):
    server.register_blueprint(main_routes)
    return server
