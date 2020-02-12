from mySync.config.errorpage import init_error_page
from mySync.config.routes import add_route_getroutes
from mySync.config.settings import settings


def init_config(server):
    # db uri db_type+driver://username:password@host:port/dbname
    # mysql+pymysql://root:password@localhost:3306/database_name
    server.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

    init_error_page(server)
    add_route_getroutes(server)

    return server
