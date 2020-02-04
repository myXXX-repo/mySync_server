# from flask import Flask
from .Markdown_block import Markdown_block
from .Sticky_block import Sticky_block
from .Test_block import Test_block
from .Config_block import Config_block
from .mainpage import mainpage
from .errorpage import init_error_page


# app = Flask(__name__)

def init_view(app):
    app.register_blueprint(mainpage)
    app.register_blueprint(Config_block)
    app.register_blueprint(Sticky_block)
    app.register_blueprint(Test_block)
    app.register_blueprint(Markdown_block)
    init_error_page(app)

    return app

# if __name__ == '__main__':
#     app = Flask(__name__)
#     app = init_view(app=app)
#     app.run()
