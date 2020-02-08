from mySync.config.errorpage import init_error_page
from mySync.config.routes import getroute


def init_config(server):
    # db uri db_type+driver://username:password@host:port/dbname
    # mysql+pymysql://root:password@localhost:3306/database_name
    server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/data.db'
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    server.config['app_config'] = []

    init_error_page(server)
    getroute(server)

    return server
