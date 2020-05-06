from flask import request, abort

from flask_restful import Resource

from flask import Blueprint, jsonify
from flask_restful import Api

from mySync.common.access_token_check import check_access_token

notify = []


class Notify_list(Resource):
    @check_access_token
    def get(self):
        return jsonify(notify)

    @check_access_token
    def post(self):
        must_exist_keys = ["notify_time", "con", "dev_name"]
        request_data = None
        if request.json is not None:
            # 使用json发送多条notify
            request_data = request.json

            #    确保发来的数据解析完成是个list
            if not isinstance(request_data, list):
                return abort(400)

            # 确保发来的数据中每个item都有完整的结构
            for ii in request_data:
                for i in ii:
                    if i not in must_exist_keys:
                        return abort(400)

            # 将发来的 经过检验的数据添加到后面
            for i in request_data:
                notify.append(i)

            return "add items done"
        else:
            # 使用args发送单条notify
            request_data = request.form.to_dict()
            if request_data == {}:
                request_data = request.args.to_dict()
            # return jsonify(request_data)
            # 确保发来的数据有完整的结构
            for i in must_exist_keys:
                if i not in request_data:
                    return abort(400)

            # 添加到数据结构中
            notify.append(request_data)
            return "add item done"

    @check_access_token
    def delete(self):
        global notify
        notify = []
        return "delete all done"


Notify_routes = Blueprint('Notify_routes', __name__)

Notify_api = Api(Notify_routes)

Notify_api.add_resource(Notify_list, '/app/Notifies')


@Notify_routes.route('/app/Notify/<int:id_id>', methods=['GET'])
@check_access_token
def get_item_by_id(id_id):
    if id_id not in range(0, len(notify)):
        return abort(404)
    return jsonify(notify[id_id])


@Notify_routes.route('/app/Notifies/get_len', methods=['GET'])
def get_len():
    return str(len(notify))


@Notify_routes.route('/app/Notify/test', methods=['GET'])
def test():
    return "server is fine"
