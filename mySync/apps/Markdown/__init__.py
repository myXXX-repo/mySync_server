from mySync.apps.Markdown.routes import Markdown_routes


def init_app_Markdown(server):
    server.register_blueprint(Markdown_routes)
    # server.config['app_config']['Markdown']={
    #     'MARKDOWN_'
    # }
    return server
