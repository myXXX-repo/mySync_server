def init_setting(app):
    # db uri db_type+driver://username:password@host:port/dbname
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
