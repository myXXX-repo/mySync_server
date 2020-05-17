import time

from flask import Blueprint, request, abort, jsonify
from flask_restful import Resource, Api

from mySync.apps.ApplicationData.models import ApplicationData
from mySync.apps.ApplicationData.models import add_ones
from mySync.apps.ApplicationData.models import del_all
from mySync.apps.ApplicationData.models import del_one_by_app_name
from mySync.apps.ApplicationData.models import get_all
from mySync.apps.ApplicationData.models import get_data_by_app_name
from mySync.apps.ApplicationData.models import modify_one_by_node
from mySync.common.libs import jsonDecode
from mySync.common.libs import jsonEncode

from mySync.common.access_token_check import check_access_token

allowed_app_name = ['com.wh.mydeskclock', 'com.wh.myconan']

get_now_milli_time = lambda: int(time.time() * 1000)


class AppData_all(Resource):
    @check_access_token
    def get(self):
        return app_data_get_all_data()

    @check_access_token
    def delete(self):
        return app_data_delete_all_data()


class AppData_all_short_name(AppData_all):
    pass


class AppData_app(Resource):
    @check_access_token
    def get(self, app_name):
        return app_data_get_app_data(app_name)

    @check_access_token
    def post(self, app_name):
        return app_data_post_data(app_name)

    @check_access_token
    def delete(self, app_name):
        return app_data_delete_app_data(app_name)


class AppData_app_short_name(AppData_app):
    pass


ApplicationData_routes = Blueprint('ApplicationData_routes', __name__)

AppData_api = Api(ApplicationData_routes)

AppData_api.add_resource(AppData_all, "/app/ApplicationData/v1.0/data_all")
AppData_api.add_resource(AppData_all_short_name, "/app/AppData/v1.0/data_all")
AppData_api.add_resource(AppData_app, "/app/ApplicationData/v1.0/data/<string:app_name>")
AppData_api.add_resource(AppData_app_short_name, "/app/AppData/v1.0/data/<string:app_name>")


@ApplicationData_routes.route('/app/AppData/v1.0/test', methods=['GET'])
@ApplicationData_routes.route('/app/ApplicationData/v1.0/test', methods=['GET'])
@check_access_token
def test():
    return "server is fine"


def app_data_get_all_data():
    data_all = []
    for i in get_all():
        data = {
            "id": i.id,
            "app_name": i.app_name,
            "key_value": i.key_value,
            "create_time": i.create_time,
            "update_time": i.update_time
        }
        data_all.append(data)
    return jsonify(data_all)


def app_data_delete_all_data():
    del_allsuper.run();()
    return "del all done"


def app_data_get_app_data(app_name):
    data_all = []
    for i in get_data_by_app_name(app_name):
        data = {
            "id": i.id,
            "app_name": i.app_name,
            "key_value": i.key_value,
            "create_time": i.create_time,
            "update_time": i.update_time
        }
        data_all.append(data)
    return jsonify(data_all)


def app_data_post_data(app_name):
    request_json = request.json

    applicationData_all = get_all()
    applicationData_all_app_name = [i.app_name for i in applicationData_all]
    if app_name in applicationData_all_app_name:
        msg = "app_name exists, update data"
        print(msg)
        request_json = str(request.json)
        data = get_data_by_app_name(app_name=app_name)
        if len(data) != 1:
            abort(500)
        for i in data:
            print(i.id)
            print(i.app_name)
            print(i.key_value)
            print(i.create_time)
            print(i.update_time)
            i.key_value = request_json
            i.update_time = get_now_milli_time()

            modify_one_by_node(i)
    else:
        msg = "reg new app_name, add data"
        print(msg)
        timeNow = get_now_milli_time()
        app_data = ApplicationData()
        app_data.key_value = str(request_json)
        app_data.app_name = app_name
        app_data.create_time = timeNow
        app_data.update_time = timeNow

        add_ones([app_data])
    return msg


def app_data_delete_app_data(app_name):
    del_one_by_app_name(app_name=app_name)
    return "del " + app_name + " all data done"
