# from flask import Flask
from .mainpage import mainpage
from .configpage import config
from .errorpage import init_error_page


# app = Flask(__name__)

def init_view(app):
    app.register_blueprint(mainpage)
    app.register_blueprint(config)

    init_error_page(app)

    return app


# if __name__ == '__main__':
#     app = Flask(__name__)
#     app = init_view(app=app)
#     app.run()
