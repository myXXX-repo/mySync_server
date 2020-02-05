from json import dumps as jsonencode


def addroute(app):
    @app.route('/getroutes', methods=['GET'])
    def config_getroutes():
        url_map = str(app.url_map)[5:-2]
        url_map = url_map.split('<Rule')[1:]
        url_map_tmp = []
        for i in range(len(url_map) - 1):
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
            route_node = {
                'route': url_map_tmp_1_route[i],
                'methods': url_map_tmp_2_method[i].split(', '),
                'endpoint': url_map_tmp_3_endpoint[i]}
            route.append(route_node)
        return jsonencode(route)
    return app
