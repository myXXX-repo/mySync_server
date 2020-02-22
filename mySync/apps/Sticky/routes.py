from flask import Blueprint, request, abort, render_template

from mySync.apps.Sticky.models import Sticky, db_insert
from mySync.common.libs import DataArray
from json import dumps as jsonencode

Sticky_routes = Blueprint('Sticky_routes', __name__)


# def db_delete(key,value):
#     pass
#
# def db_update(data=[]):
#     pass
#
# def db_show():
#     pass

@Sticky_routes.route('/StickyIndex')
def StickyIndex():
    return render_template('index_sticky.html', title1='Sticky', title2='Index')


@Sticky_routes.route('/Sticky/test/<cmd>')
def sticky_test(cmd):
    if cmd == 'addsticky':
        db_insert('t', 'c', 't', 'd', 'i')
        return 'add done'
    else:
        return abort(404)


@Sticky_routes.route(
    '/v<float:version>/Sticky',
    methods=['GET', 'POST', 'DELETE'])
def get_post_res_list(version):
    # sticky = DataArray('data/Sticky.json')

    if version == 1.0:
        return abort(410)
    elif version == 2.0:
        return abort(410)

    # ------------------------------------------
    #   @uri: http://host:port/v2.1/Sticky
    #   @methods: GET POST DELETE
    # ------------------------------------------
    elif version == 2.1:
        access_method = request.method

        # GET: 获取整个数据资源列表json数组格式
        if access_method == 'GET':
            data_to_return = []
            request_data = request.args.to_dict()  # 用于保存获取数据的过滤



            if 'limit' in request_data:
                # sticky_data = sticky.dataArray
                limit = 0
                try:
                    limit = int(request_data['limit'])
                except Exception as err:
                    print(err)
                    return abort(400)

                # data_to_return = sticky_data[0:int(limit)]
            else:
                pass
                # data_to_return = sticky.dataArray
            # return jsonencode(data_to_return)

            return jsonencode({'data': [
                {
                    'title': "this is title",
                    'con': "this is con"
                }
            ]})

        # POST: 添加资源
        elif access_method == 'POST':
            request_data = request.values.to_dict()

            if len(request_data) != set(request_data):
                print("got repeated keys")
                return abort(400)

            keys = ['title', 'con', 'time', 'devName', 'ip']
            for key in keys:
                if key not in request_data:
                    print("got missing key(s)")
                    return abort(400)
            db_insert(title=request_data['title'],
                      con=request_data['con'],
                      time=request_data['time'],
                      devName=request_data['devName'],
                      ip=request_data['ip'])
            return "Success"

        elif access_method == 'DELETE':
            # delete all
            pass
    else:
        return abort(404)


@Sticky_routes.route(
    '/v<float:version>/Sticky/<int:resid_raw>',
    methods=['GET', 'PUT', 'PATH', 'DELETE'])
def get_put_path_res_by_id(version, resid_raw):
    sticky = DataArray('data/Sticky.json')
    access_method = request.method

    if version == 1.0:
        return abort(410)
    elif version == 2.0:
        return abort(410)

    # ------------------------------------------
    #   @uri: http://host:port/v2.1/Sticky/0
    #   @methods: GET PUT PATH DELETE
    # ------------------------------------------
    elif version == 2.1:

        resid = resid_raw

        # 如果id超出数据长度
        # 则返回错误代码404
        if resid not in range(len(sticky.dataArray)):
            return abort(404)

        # GET: 返回json格式的一条数据
        if access_method == 'GET':
            return jsonencode(sticky.dataArray)

        # PUT: 收到完整的数据 覆盖制定id数据
        elif access_method == 'PUT' or access_method == 'PATH':
            request_data = request.args.to_dict()
            # TODO add function to check data
            sticky.dataArray[resid].update(request_data)
            return 'update success'
        elif access_method == 'DELETE':
            sticky.delbyId(resid)
            return 'deleted success'

        else:
            return abort(405)
