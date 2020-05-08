import time

from flask import Blueprint, request, abort, jsonify
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

ApplicationData_routes = Blueprint('ApplicationData_routes', __name__)

allowed_app_name = ['com.wh.mydeskclock', 'com.wh.myconan']

get_now_milli_time = lambda: int(time.time() * 1000)


# id app_name key_value create_time update_time

# http://ip:port/app/ApplicationData/v1.0/test GET   for testing
# http://ip:port/app/ApplicationData/v1.0/all_data GET    get all data from sql
# http://ip:port/app/ApplicationData/v1.0/data/<string:app_name> get   all data by


# 测试连接

@ApplicationData_routes.route('/app/ApplicationData/v1.0/test', methods=['GET'])
@check_access_token
def test():
    return "server is fine"


# get delete 全部数据
@ApplicationData_routes.route('/app/ApplicationData/v1.0/all_data', methods=['GET', 'DELETE'])
@check_access_token
def get_delete_all_data():
    request_method = request.method
    if request_method == 'GET':
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
        return jsonEncode(data_all)
    elif request_method == 'DELETE':
        del_all()
        return "del all done"


# get post delete 指定app的全部数据
@ApplicationData_routes.route('/app/ApplicationData/v1.0/data/<string:app_name>', methods=['GET', 'POST', 'DELETE'])
@check_access_token
def get_post_delete_data(app_name):
    if app_name not in allowed_app_name:
        print(app_name)
        abort(403)

    request_method = request.method
    # 获取 某app的全部数据
    if request_method == 'GET':
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

    # 上传某app的全部数据
    elif request_method == 'POST':
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
    elif request_method == 'DELETE':
        del_one_by_app_name(app_name=app_name)
        return "del " + app_name + " all data done"

# @ApplicationData_routes.route('/app/ApplicationData/v1.0/delete', methods=['DELETE'])
# def del_all_data():
#     del_all()
#     return "del all done"
#
#
# @ApplicationData_routes.route('/app/ApplicationData/v1.0/<string:app_name>/delete', methods=['DELETE'])
# def del_data_by_app_name(app_name):
#     del_one_by_app_name(app_name)
#     return "del " + app_name + " all data done"

# def itemInDB(data_all, data_item):
#     data_all_app_name = []
#     data_all_data_key = []
#     for i in data_all:
#         data_all_app_name.append(i['app_name'])
#         data_all_data_key.append(i['data_key'])
#
#     if data_item['app_name'] not in data_all_app_name:
#         return False
#     elif data_item['data_key'] not in data_all_data_key:
#         return False
#     else:
#         # update data
#         return True
