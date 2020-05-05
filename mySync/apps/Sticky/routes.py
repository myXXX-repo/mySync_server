from flask import Blueprint, request, abort, render_template, jsonify

from flask_restful import Api, Resource

from mySync.apps.Sticky.models import Sticky, getAll, add_ones, del_all
from mySync.common.access_token_check import check_access_token
from mySync.common.libs import DataArray
from json import dumps as json_encode


# operate with id
class Sticky_item(Resource):
    @check_access_token
    def get(self):
        pass

    @check_access_token
    def post(self):
        pass

    @check_access_token
    def delete(self):
        pass


# operate
class Sticky_list(Resource):
    @check_access_token
    def get(self):
        sticky_list = []
        for i in getAll():
            item = {
                'id': i.id,
                'title': i.title,
                'con': i.con,
                'dev_name': i.dev_name,
                'create_time': i.create_time,
                'update_time': i.update_time
            }
            sticky_list.append(item)
        return jsonify(sticky_list)

    @check_access_token
    def post(self):
        if request.json is not None:
            # TODO 将json转换成数组 with function jsonDecode()
            # TODO 检查json中每个对象的数据完整性 不完整则返回错误
            return request.json
        else:
            request_args = request.args.to_dict()
            s = Sticky()
            s.title = 'title'
            s.dev_name = 'mac mimi'
            s.con = '[{time:...,con...},{},{},{},...]'
            s.ip = '127.0.0.1'
            add_ones([s])
            return 'add done'

    @check_access_token
    def delete(self):
        if del_all() == 0:
            return "del done"
        else:
            return "del failed"


Sticky_routes = Blueprint('Sticky_routes', __name__)
Sticky_api = Api(Sticky_routes)
Sticky_api.add_resource(Sticky_item, '/app/Sticky/item/<int:id_id>')
Sticky_api.add_resource(Sticky_list, '/app/Sticky')


@Sticky_routes.route('/app/Sticky/test')
def Sticky_test():
    return "server is fine"

    # below here is useless

    # @Sticky_routes.route('/StickyIndex')
    # def StickyIndex():
    #     return render_template('index_sticky.html', title1='Sticky', title2='Index')

    # @Sticky_routes.route('/Sticky/test/<cmd>')
    # def sticky_test(cmd):
    #     if cmd == 'addsticky':
    #
    #     else:
    #         return abort(404)

    # @Sticky_routes.route(
    #     '/v<float:version>/Sticky',
    #     methods=['GET', 'POST', 'DELETE'])
    # def get_post_res_list(version):
    #     # sticky = DataArray('data/Sticky.json')
    #
    #     if version == 1.0:
    #         return abort(410)
    #     elif version == 2.0:
    #         return abort(410)
    #
    #     # ------------------------------------------
    #     #   @uri: http://host:port/v2.1/Sticky
    #     #   @methods: GET POST DELETE
    #     # ------------------------------------------
    #     elif version == 2.1:
    #         access_method = request.method
    #
    #         # GET: 获取整个数据资源列表json数组格式
    #         if access_method == 'GET':
    #             data_to_return = []
    #             request_data = request.args.to_dict()  # 用于保存获取数据的过滤
    #
    #             if 'limit' in request_data:
    #                 # sticky_data = sticky.dataArray
    #                 limit = 0
    #                 try:
    #                     limit = int(request_data['limit'])
    #                 except Exception as err:
    #                     print(err)
    #                     return abort(400)
    #
    #                 # data_to_return = sticky_data[0:int(limit)]
    #             else:
    #                 pass
    #                 # data_to_return = sticky.dataArray
    #             # return jsonencode(data_to_return)
    #
    #             return json_encode({'data': [
    #                 {
    #                     'title': "this is title",
    #                     'con': "this is con",
    #                     'type': "RealSticky"
    #                 }, {
    #                     'title': "this is title",
    #                     'con': "this is con",
    #                     'type': "RealSticky"
    #                 }, {
    #                     'title': "this is title",
    #                     'con': "this is con",
    #                     'type': "TODO"
    #                 }, {
    #                     'title': "this is title",
    #                     'con': "this is con",
    #                     'type': "Tabs"
    #                 },
    #             ]})
    #
    #
    #         # POST: 添加资源
    #         elif access_method == 'POST':
    #             request_data = request.values.to_dict()
    #
    #             if len(request_data) != set(request_data):
    #                 print("got repeated keys")
    #                 return abort(400)
    #
    #             keys = ['title', 'con', 'time', 'devName', 'ip']
    #             for key in keys:
    #                 if key not in request_data:
    #                     print("got missing key(s)")
    #                     return abort(400)
    #             db_insert(title=request_data['title'],
    #                       con=request_data['con'],
    #                       time=request_data['time'],
    #                       dev_name=request_data['devName'],
    #                       ip=request_data['ip'])
    #             return "Success"
    #
    #         elif access_method == 'DELETE':
    #             # delete all
    #             pass
    #     else:
    #         return abort(404)
    #
    #
    # @Sticky_routes.route(
    #     '/v<float:version>/Sticky/<int:resid_raw>',
    #     methods=['GET', 'PUT', 'PATH', 'DELETE'])
    # def get_put_path_res_by_id(version, resid_raw):
    #     sticky = DataArray('data/Sticky.json')
    #     access_method = request.method
    #
    #     if version == 1.0:
    #         return abort(410)
    #     elif version == 2.0:
    #         return abort(410)
    #
    #     # ------------------------------------------
    #     #   @uri: http://host:port/v2.1/Sticky/0
    #     #   @methods: GET PUT PATH DELETE
    #     # ------------------------------------------
    #     elif version == 2.1:
    #
    #         resid = resid_raw
    #
    #         # 如果id超出数据长度
    #         # 则返回错误代码404
    #         if resid not in range(len(sticky.dataArray)):
    #             return abort(404)
    #
    #         # GET: 返回json格式的一条数据
    #         if access_method == 'GET':
    #             return json_encode(sticky.dataArray)
    #
    #         # PUT: 收到完整的数据 覆盖制定id数据
    #         elif access_method == 'PUT' or access_method == 'PATH':
    #             request_data = request.args.to_dict()
    #             # TODO add function to check data
    #             sticky.dataArray[resid].update(request_data)
    #             return 'update success'
    #         elif access_method == 'DELETE':
    #             sticky.delbyId(resid)
    #             return 'deleted success'
    #
    #         else:
    #             return abort(405)
