from mySync.common.ext import db


class ApplicationData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_name = db.Column(db.String(1024))
    key_value = db.Column(db.Text)
    create_time = db.Column(db.String(1024))
    update_time = db.Column(db.String(1024))


def add_ones(datas=None):
    if datas is None:
        datas = []
    for i in datas:
        db.session.add(i)
    db.session.commit()


def get_all():
    return ApplicationData.query.all()


def get_data_by_app_name(app_name):
    return ApplicationData.query.filter_by(app_name=app_name).all()


def del_one(application_data):
    db.session.delete(application_data)
    db.session.commit()


def del_one_by_app_name(app_name):
    try:
        db.session.query(ApplicationData).filter(ApplicationData.app_name == app_name).delete()
    except:
        db.session.rollback()
    finally:
        db.session.commit()


# def del_all_by_app_name(app_name):
#     try:
#         db.session.query(ApplicationData).filter(ApplicationData.app_name == app_name).delete()
#     except:
#         db.session.rollback()
#     finally:
#         db.session.commit()


def del_all():
    try:
        db.session.query(ApplicationData).delete()
    except:
        db.session.rollback()
    finally:
        db.session.commit()


# def get_one_by_id(item_id):
#     return ApplicationData.query.filter_by(id=item_id) \
#         .first_or_404()

def modify_one_by_node(node):
    appData = ApplicationData.query.get(node.id)
    appData.key_value = node.key_value
    appData.app_name = node.app_name
    appData.create_time = node.create_time
    appData.update_time = node.update_time

    db.session.commit()
