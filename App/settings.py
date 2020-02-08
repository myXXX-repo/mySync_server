def init_setting(app):
    # db uri db_type+driver://username:password@host:port/dbname
    # mysql+pymysql://root:password@localhost:3306/database_name
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
