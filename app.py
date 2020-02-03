from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from flask import abort
import os
import json
import time
import argparse
from FileCtrl import FileCtrl
from DataArray import DataArray
from werkzeug.utils import secure_filename

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = './data'
# ALLOWED_EXTENSIONS = set(['txt'])


# re_define error page
@app.errorhandler(400)
def error_400(e):
    errorcode = 400
    return render_template('error_page.html', error_code=errorcode, error_msg="BadRequest"), errorcode


@app.errorhandler(401)
def error_401(e):
    errorcode = 401
    return render_template('error_page.html', error_code=errorcode, error_msg="Unauthorized"), errorcode


@app.errorhandler(403)
def error_403(e):
    errorcode = 403
    return render_template('error_page.html', error_code=errorcode, error_msg="Forbidden"), errorcode


@app.errorhandler(404)
def error_404(e):
    errorcode = 404
    return render_template('error_page.html', error_code=errorcode, error_msg="NotFound"), errorcode


@app.errorhandler(405)
def error_405(e):
    errorcode = 405
    return render_template('error_page.html', error_code=errorcode, error_msg="MethodNotAllowed"), errorcode


@app.errorhandler(406)
def error_406(e):
    errorcode = 406
    return render_template('error_page.html', error_code=errorcode, error_msg="NotAcceptable"), errorcode


@app.errorhandler(408)
def error_408(e):
    errorcode = 408
    return render_template('error_page.html', error_code=errorcode, error_msg="RequestTimeout"), errorcode


@app.errorhandler(409)
def error_409(e):
    errorcode = 409
    return render_template('error_page.html', error_code=errorcode, error_msg="Conflict"), errorcode


@app.errorhandler(410)
def error_410(e):
    errorcode = 410
    return render_template('error_page.html', error_code=errorcode, error_msg="Gone"), errorcode


@app.errorhandler(411)
def error_411(e):
    errorcode = 411
    return render_template('error_page.html', error_code=errorcode, error_msg="LengthRequired"), errorcode


@app.errorhandler(412)
def error_412(e):
    errorcode = 412
    return render_template('error_page.html', error_code=errorcode, error_msg="InternalServerError"), errorcode


@app.errorhandler(413)
def error_413(e):
    errorcode = 413
    return render_template('error_page.html', error_code=errorcode, error_msg="RequestEntityTooLarge"), errorcode


@app.errorhandler(414)
def error_414(e):
    errorcode = 414
    return render_template('error_page.html', error_code=errorcode, error_msg="RequestURITooLarge"), errorcode


@app.errorhandler(416)
def error_416(e):
    errorcode = 416
    return render_template('error_page.html', error_code=errorcode, error_msg="RequestedRangeNotSatisfiable"), errorcode


@app.errorhandler(417)
def error_417(e):
    errorcode = 417
    return render_template('error_page.html', error_code=errorcode, error_msg="ExpectationFailed"), errorcode


@app.errorhandler(500)
def error_500(e):
    errorcode = 500
    return render_template('error_page.html', error_code=errorcode, error_msg="InternalServerError"), errorcode


@app.errorhandler(501)
def error_501(e):
    errorcode = 501
    return render_template('error_page.html', error_code=errorcode, error_msg="NotImplemented"), errorcode


@app.errorhandler(502)
def error_502(e):
    errorcode = 502
    return render_template('error_page.html', error_code=errorcode, error_msg="BadGateway"), errorcode


@app.errorhandler(503)
def error_503(e):
    errorcode = 503
    return render_template('error_page.html', error_code=errorcode, error_msg="ServiceUnavailable"), errorcode


@app.errorhandler(504)
def error_504(e):
    errorcode = 504
    return render_template('error_page.html', error_code=errorcode, error_msg="GatewayTimeout"), errorcode


@app.errorhandler(505)
def error_505(e):
    errorcode = 505
    return render_template('error_page.html', error_code=errorcode, error_msg="HTTPVersionNotSupported"), errorcode


# class Statistics:
#     def __init__(self):
#         self.apis = []

#         self.fileCtrl = FileCtrl("data/Statistics.json")
#         jsonDatatmp = self.fileCtrl.read(AUTOCREATE=1)
#         if jsonDatatmp != "":
#             self.apis = json.loads(jsonDatatmp)
#         else:
#             pass
#             # self.createDataBody()


# statistics = Statistics()


sticky = DataArray("data/sticky.json")

# re_define route


@app.route('/')
def index():
    # statistics.rec('Index', 'IndexPage', request.method)
    return render_template('index.html', title1="mySync", title2="index")


@app.route('/v<float:version>/<app>', methods=['GET', 'POST', 'DELETE'])
def get_post_res_list(version, app):
    if version == 2.1:  # post data with form
        access_method = request.method
        # ------------------------------------------
        #   @uri: http://host:port/v2.1/Sticky
        #   @methods: GET POST DELETE
        # ------------------------------------------
        if app == 'Sticky':

            # GET: 获取整个数据资源列表json数组格式
            if access_method == 'GET':  # 获取资源
                data_to_return = []  # 初始化用于返回的资源列表
                request_data = request.args.to_dict()  # 用于保存获取数据的过滤
                if 'limit' in request_data:
                    sticky_data = sticky.dataArray
                    # TODO 加上一些异常处理 确保limit的值正确
                    data_to_return = sticky_data[0:int(request_data['limit'])]
                else:
                    data_to_return = sticky.dataArray

                return json.dumps(data_to_return)

            elif access_method == 'POST':  # 添加资源
                request_data = request.values.to_dict()
                newdata = {}
                keylist = ['title', 'con', 'time', 'devName', 'ip']
                if 'title' in request_data:
                    if 'con' in request_data:
                        if 'time' in request_data:
                            if 'devName' in request_data:
                                if 'ip' in request_data:
                                    newdata = {
                                        keylist[i]: request_data[keylist[i]] for i in range(len(keylist))}
                                    sticky.add(newdata)
                                    return "Success"
                return "error get wrong data"

            elif access_method == 'DELETE':
                sticky.dataArray = []
                return str(sticky.dataArray)

            else:
                abort(405)  # method not allowed

        elif app == 'tabSync':
            pass
        elif app == 'file':
            print(str(request))
            # print(request.method)
            print(request.files.to_dict())
            file = request.files['file']
            print(file)
            # print(file.filename.to_dict())
            return request.method

        elif app == 'markdown':
            if access_method == 'GET':
                return json.dumps(os.listdir('data/markdown'))
            elif access_method == 'POST':
                abort(404)
            pass
        else:
            abort(404)

    else:
        abort(404)


@app.route('/v<float:version>/<app>/<resid_raw>', methods=['GET', 'PUT', 'PATH', 'DELETE'])
def get_put_path_res_by_id(version, app, resid_raw):
    if version == 2.1:
        access_method = request.method
        if app == 'Sticky':
            # ------------------------------------------
            #   @uri: http://host:port/v2.1/Sticky/0
            #   @methods: GET PUT PATH DELETE
            # ------------------------------------------
            resid = 0
            # 将资源id转成int类型
            # 如果resid_raw转换失败
            # 则抛出异常并返回400
            try:
                resid = int(resid_raw)
            except Exception as e:
                print(e)
                abort(400)

            # 如果id超出数据长度
            # 则返回错误代码404
            if resid not in range(len(sticky.dataArray)):
                abort(404)

            # 判断method

            # GET: 返回json格式的一条数据
            if access_method == 'GET':  # 获取指定的一条资源 by id
                return json.dumps(sticky.dataArray)

            # PUT: 收到完整的数据 覆盖制定id数据
            elif access_method == 'PUT':
                request_data = request_data.args.to_dict()
                # TODO add function to check data
                sticky.dataArray[resid].update(request_data)
                return 'cover success'

            # PATH: 收到一条增量数据更新资源
            elif access_method == 'PATH':
                request_data = request_data.args.to_dict()
                # TODO add function to check data
                sticky.dataArray[resid].update(request_data)
                return 'update success'

            # DELETE: 删除指定id的资源
            elif access_method == 'DELETE':
                sticky.delbyId(resid)
                return 'deleted success'
            else:  # end of method switch
                abort(405)

        # ------------------------------------------
        #   @uri: http://host:port/v2.1/file/0
        #   @methods: GET PUT PATH DELETE
        # ------------------------------------------
        elif app == 'file':
            print(request.method)
            return request.method

        # ------------------------------------------
        #   @uri: http://host:port/v2.1/markdown/test.md
        #   @methods: GET PUT DELETE
        # ------------------------------------------
        elif app == 'markdown':
            resid = secure_filename(resid_raw)
            markdownstr = ''
            try:
                with open('data/markdown/' + resid, 'r') as filefd:
                    markdownstr = json.dumps(filefd.read())
            except Exception as err:
                print(err)
                abort(404)

            # GET
            if access_method == 'GET':
                request_data = request.args.to_dict()
                if 'type' in request_data:
                    if request_data['type'] == 'html':
                        # TODO return html page
                        return render_template('temp_markdown.html', title1='mySync', title2='MD', markdownstr=markdownstr[1:-1])
                return json.dumps(markdownstr)

            # PUT
            # TODO 判断接收到的数据是否完整 否则返回400
            # TODO 判断数据文件夹是否存在
            # TODO 判断相应数据文件是否存在
            # TODO 不存在则返回404
            # TODO 存在则将数据覆盖后返回success

            # 不支持 PATH
            # TODO 返回405

            # DELETE
            # TODO 判断请求数据是否完整 否则返回400
            # TODO 数据文件是否存在
            # TODO 不存在返回404
            # TODO 存在则将文件删除后返回
            pass

        else:  # end of app switch
            abort(404)

    else:  # end of version switch
        abort(404)


@app.route('/statistics', methods=['GET'])
def getStatistics():
    # statistics.rec('statistics', 'statistics',   request.method)
    # return json.dumps(statistics.apis)
    abort(404)


@app.route('/config', methods=['GET'])
def config():
    return render_template("config.html", title1="mySync", title2="config")


@app.route('/config/reset/<appname>', methods=['GET'])
def config_reset(appname):
    if appname == 'Sticky':
        pass
    if appname == 'tabSync':
        pass
    if appname == 'toDoList':
        pass
    if appname == 'statistics':
        pass


@app.route('/config/getroutes', methods=['GET'])
def config_getroutes():
    url_map = str(app.url_map)[5:-2]
    url_map = url_map.split('<Rule')[1:]
    url_map_tmp = []
    for i in range(len(url_map)-1):
        a = url_map[i][1:-3]
        url_map_tmp.append(a)
    url_map_tmp.append(url_map[-1][1:])

    url_map_tmp_1_route = []
    url_map_tmp_2_method = []
    url_map_tmp_3_endpoint = []
    for i in url_map_tmp:
        tmp = i.split('->')
        tmp_tmp = tmp[0].split('(')
        url_map_tmp_1_route.append(tmp_tmp[0][1:-2])
        url_map_tmp_2_method.append(tmp_tmp[1][:-2])
        url_map_tmp_3_endpoint.append(tmp[1][1:-1])
    route = []
    for i in range(len(url_map_tmp_1_route)):
        route_node = {}
        route_node['route'] = url_map_tmp_1_route[i]
        route_node['methods'] = url_map_tmp_2_method[i].split(', ')
        route_node['endpoint'] = url_map_tmp_3_endpoint[i]
        route.append(route_node)
    return json.dumps(route)


@app.route('/test/markdown')
def test_markdown():
    mdjson = ''
    with open('data/markdown/test.md', 'r') as filefd:
        mdjson = json.dumps(filefd.read())
    return render_template('index_markdown.html', title1='mySync', title2='md',
                           # markdownjson=mdjson[1:-1]
                           )


@app.route('/test/errorpage/<error_code>')
def test_error_page(error_code):
    return abort(int(error_code))


@app.route('/test/request')
def test_request():
    return render_template("test_request.html", title1="mySync", title2="testrequest")


@app.route('/getip')
def getip():
    return request.remote_addr


parser = argparse.ArgumentParser(
    # description='Test for argparse'
)
parser.add_argument('-l', '--listen', default="0.0.0.0")
parser.add_argument('-p', '--port', default=5000)
parser.add_argument('-d', '--debugOn', default=True)
args = parser.parse_args()

if __name__ == "__main__":
    try:
        app.run(
            host=args.listen,
            debug=args.debugOn,
            port=args.port,
            threaded=True
        )
    except Exception as e:
        print(e)
