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

app = Flask(__name__)


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


# re_define route

class FileCtrl:  # ctrl file
    def __init__(self, filePath, fileFolder='data'):
        if os.path.exists(fileFolder):
            pass
        else:
            os.mkdir(fileFolder)
        self.filePath = filePath

    def write_append(self, str):
        with open(self.filePath, 'a') as filefd:
            filefd.write(str+'\n')

    def write_cover(self, str):
        with open(self.filePath, 'w') as filefd:
            filefd.write(str)

    def read(self, AUTOCREATE=0):
        data_to_return = ""
        if os.path.isfile(self.filePath):
            # if file exists
            # read file and return data
            with open(self.filePath, 'r') as filefd:
                data_to_return = filefd.read()
        else:
            # if file not exists
            if AUTOCREATE == 1:
                with open(self.filePath, 'w') as filefd:
                    filefd.write("")
                pass
        return data_to_return


class Statistics:
    def __init__(self):
        self.apis = []
        self.fileCtrl = FileCtrl("data/Statistics.json")
        jsonDatatmp = self.fileCtrl.read(AUTOCREATE=1)
        if jsonDatatmp != "":
            self.apis = json.loads(jsonDatatmp)
        else:
            self.createDataBody()

    def rec(self, appname, apiname, method):
        for app in self.apis:
            if app["appname"] == appname:
                for api in app["apis"]:
                    if api['apiname'] == apiname:
                        if api['method'] == method:
                            api['NumOfCall'] += 1
                            api['LastCallTime'] = str(time.strftime(
                                '%Y-%m-%d %H:%M:%S', time.localtime()))
                            self.fileCtrl.write_cover(json.dumps(self.apis))
                            return
        return

    def createDataBody(self):
        bodySeed = [
            ['Index', [
                ['IndexPage', ['GET']]
            ]],
            ['Sticky', [
                ['StickyIndex', ['GET']],
                ['getSticky', ['GET']],
                ['addSticky', ['POST']],
                ['delSticky', ['GET']],
                ['clearSticky', ['GET']],
            ]],
            ['statistics', [
                ['statistics', ['GET']]
            ]],
        ]
        for app in bodySeed:
            appnodetmp = {}
            appnodetmp["appname"] = app[0]
            appnodetmp["apis"] = []
            for api in app[1]:
                for method in api[1]:
                    apinodetmp = {}
                    apinodetmp["apiname"] = api[0]
                    apinodetmp["method"] = method
                    apinodetmp["NumOfCall"] = 0
                    apinodetmp["LastCallTime"] = "N/A"
                    appnodetmp["apis"].append(apinodetmp)
            self.apis.append(appnodetmp)


statistics = Statistics()


class DataArray:
    def __init__(self, filePath):
        self.dataArray = []
        self.fileCtrl = FileCtrl(filePath)
        jsonDatatmp = self.fileCtrl.read(AUTOCREATE=1)
        if jsonDatatmp != "":
            self.dataArray = json.loads(jsonDatatmp)

    def get(self):
        return self.dataArray

    def getbyId(self, id):
        return self.dataArray[id]

    def add(self, new):
        self.dataArray.append(new)
        self.fileCtrl.write_cover(json.dumps(self.dataArray))

    def clear(self):
        self.dataArray = []
        self.fileCtrl.write_cover(json.dumps(self.dataArray))

    def delbyId(self, id):
        self.dataArray.pop(int(id))
        self.fileCtrl.write_cover(json.dumps(self.dataArray))


sticky = DataArray("data/sticky.json")


@app.route('/')
def index():
    statistics.rec('Index', 'IndexPage', request.method)
    return render_template('index.html', title1="mySync", title2="index")


@app.route('/t', methods=['GET', 'post', 'PUT', 'PATH'])
def index_t():
    return request.args.to_dict()

# app_sticky


@app.route('/v<float:version>/<app>', methods=['GET', 'POST'])
def get_post_res(version, app):
    if version == 2.1:  # post data with form
        if app == 'Sticky':
            access_method = request.method
            if access_method == 'GET':  # 获取资源
                data_to_return = []
                request_data = request.args.to_dict()  # 用于保存获取数据的过滤
                if 'limit' in request_data:
                    sticky_data = sticky.dataArray
                    data_to_return = sticky_data[0:int(request_data['limit'])]
                else:
                    data_to_return = sticky.dataArray

                return json.dumps(data_to_return)

            elif access_method == 'POST':  # 添加资源
                request_data = request.values.to_dict()
                newdata = {}
                if 'title' in request_data:
                    if 'con' in request_data:
                        if 'time' in request_data:
                            if 'devName' in request_data:
                                if 'ip' in request_data:
                                    newdata['title'] = request_data['title']
                                    newdata['con'] = request_data['con']
                                    newdata['time'] = request_data['time']
                                    newdata['devName'] = request_data['devName']
                                    newdata['ip'] = request_data['ip']
                                    sticky.add(newdata)
                                    return "Success"
                else:
                    return "error get wrong data"
            else:
                abort(405)  # method not allowed

        elif app == 'tabSync':
            pass

        else:
            abort(404)

    else:
        abort(404)


@app.route('/v<float:version>/<app>/<int:resid>', methods=['GET', 'PUT', 'PATH', 'DELETE'])
def get_put_path_res_by_id(version, app, resid):
    if version == 2.1:
        if app == 'Sticky':
            if resid not in range(len(sticky.dataArray)):
                abort(404)
            access_method = request.method
            if access_method == 'GET':  # 获取指定的一条资源 by id
                return json.dumps(sticky.dataArray)

            elif access_method == 'PUT':  # 发送一条完整数据覆盖指定资源
                request_data = request_data.args.to_dict()
                # TODO add function to check data
                sticky.dataArray[resid].update(request_data)
                return 'cover success'

            elif access_method == 'PATH':  # 发送一条增量数据更新资源
                request_data = request_data.args.to_dict()
                # TODO add function to check data
                sticky.dataArray[resid].update(request_data)
                return 'update success'

            elif access_method == 'DELETE':  # 删除一条数据
                sticky.delbyId(resid)
                return 'deleted success'
            else:  # end of method judge
                abort(405)

        else:  # end of app judge
            abort(404)

    else:  # end of version judge
        abort(404)


@app.route('/v2/Sticky', methods=['GET'])
def sticky_index():
    statistics.rec('Sticky', 'StickyIndex', request.method)
    return render_template('index_sticky.html', title1="Sticky", title2="index")


@app.route('/v2/Sticky/get', methods=['GET'])
def sticky_get():
    statistics.rec('Sticky', 'getSticky', request.method)
    return json.dumps(sticky.dataArray)


@app.route('/v2/Sticky/add', methods=['POST'])
def sticky_add():
    statistics.rec('Sticky', 'addSticky', request.method)
    newdata = {}
    if 'title' in request.values.to_dict():
        if 'con' in request.values.to_dict():
            if 'time' in request.values.to_dict():
                if 'devName' in request.values.to_dict():
                    if 'ip' in request.values.to_dict():
                        newdata['title'] = request.values.to_dict()['title']
                        newdata['con'] = request.values.to_dict()['con']
                        newdata['time'] = request.values.to_dict()['time']
                        newdata['devName'] = request.values.to_dict()[
                            'devName']
                        newdata['ip'] = request.values.to_dict()['ip']
                        sticky.add(newdata)
                        return "Success"
    else:
        return "error get wrong data"


@app.route('/v2/Sticky/del', methods=['GET'])
def sticky_del():
    statistics.rec('Sticky', 'delSticky', request.method)
    id_todel = request.values.to_dict()['id']
    sticky.delbyId(id_todel)
    return 'del done'


@app.route('/v2/Sticky/clear', methods=['GET'])
def sticky_clear():
    statistics.rec('Sticky', 'clearSticky', request.method)
    sticky.clear()
    return 'clear done'


@app.route('/statistics', methods=['GET'])
def getStatistics():
    statistics.rec('statistics', 'statistics', request.method)
    return json.dumps(statistics.apis)


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


@app.route('/test', methods=['GET'])
def test():
    return abort(404)


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
parser.add_argument('-d', '--debugOn', default=False)
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
