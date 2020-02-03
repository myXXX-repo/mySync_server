def init_route(app):
    @app.route('/')
    def helloworld():
        return 'helloworld'
