from flask import Blueprint
from flask import request
from flask import abort
from flask import render_template

from json import dumps as jsonencode
from json import loads as jsondecode

from os import listdir, remove
from os.path import exists
from os.path import isfile

from werkzeug.utils import secure_filename

Markdown_routes = Blueprint('Markdown_routes', __name__)

MARKDOWN_FOLDER = 'data/markdown/'


# html
@Markdown_routes.route('/MarkdownIndex')
def Markdown_index():
    return render_template('index_markdown.html', title1='Markdown', title2='Index')


@Markdown_routes.route('/MarkdownEditor')
def Markdown_editor():
    return render_template('markdown_editor.html', title1='Markdown', title2='Editor')


# -------------------------------
# api name: Markdown
# route: /v2.1/Markdown
# method: GET POST DELETE
# GET: used to get md file list
# POST: used to create file
#       with para path and con
# -----------------------------------


@Markdown_routes.route('/v<float:version>/Markdown', methods=['GET', 'POST', 'DELETE'])
def get_post_res_list(version):
    access_method = request.method

    if version == 1.0:
        return abort(410)
    elif version == 2.0:
        return abort(410)

    # ------------------------------------------
    #   @uri: http://host:port/v2.1/Markdown
    #   @methods: GET POST DELETE
    # ------------------------------------------
    elif version == 2.1:
        if access_method == 'GET':
            request_data = request.args.to_dict()
            try:
                markdown_list = jsonencode(listdir(MARKDOWN_FOLDER))
            except Exception as err:
                print(err)
                return abort(500)
            return markdown_list

        elif access_method == 'POST':
            return abort(404)

        elif access_method == 'DELETE':

            return abort(404)
        else:  # end of method
            return abort(405)

    else:  # end of version
        return abort(405)


# ----------------------------------
# api name: Markdown
# route: /v2.1/Markdown/<path:resid>
# method: GET POST DELETE
# GET: get json data from resid path
#       get with limit=? to limit data length
# POST: used to update md file
#       resid points on the exists file
#       param con have the data from client
# DELETE: used to delete exists file
#           file not found would return 404/400
# ----------------------------------


@Markdown_routes.route('/v<float:version>/Markdown/<path:resid>', methods=['GET', 'POST', 'DELETE'])
def md_test(version, resid):
    if version == 1.0:
        return abort(410)
    elif version == 2.0:
        return abort(410)
    elif version == 2.1:
        access_method = request.method
        real_path = MARKDOWN_FOLDER + resid

        if access_method == 'GET':
            # TODO need a file path secure check
            # path_node = resid.split('/')
            # path_node = [secure_filename(i) for i in path_node]
            # file_name = path_node[-1]

            if exists(real_path) and isfile(real_path):
                with open(real_path, 'r') as filefd:
                    file_con = filefd.read()
                return jsonencode(file_con)
            else:
                return abort(404)

        elif access_method == 'POST':
            request_data = request.form
            if 'con' in request_data:
                file_new_con = jsondecode(request_data['con'])
                if exists(real_path) and isfile(real_path):
                    with open(real_path, 'w') as filefd:
                        filefd.write(file_new_con)
                    return 'success'
                else:
                    return abort(404)
            else:
                return abort(400)

        elif access_method == 'DELETE':
            if exists(real_path) and isfile(real_path):
                remove(real_path)
                return 'success'
            else:
                return abort(404)
        else:  # end of method
            return abort(405)
    else:  # end of version
        return abort(404)

# @Markdown_routes.route('/markdown')
# def test():
#     return render_template('index_markdown.html', title1='mySync', title2='MD')

# @Markdown_block.route(
#     '/v<float:version>/Markdown/<resid_raw>',
#     methods=['GET', 'POST', 'DELETE'])
# def get_put_path_res_by_id(version, resid_raw):
#     access_method = request.method
#     mdfilename = secure_filename(resid_raw)
#     filefd = FileConCtrl('data/markdown/' + mdfilename)
#     markdownstr = ''

#     if version == 1.0:
#         return abort(410)
#     elif version == 2.0:
#         return abort(410)

#     # ------------------------------------------
#     #   @uri: http://host:port/v2.1/Markdown/test.md
#     #   @methods: GET POST DELETE
#     # ------------------------------------------
#     elif version == 2.1:

#         if access_method == 'GET':

#             try:  # read markdown data from file
#                 markdownstr = jsonencode(filefd.read())
#                 # print(markdownstr)
#             except Exception as err:
#                 print(err)
#                 abort(404)

#             request_data = request.args.to_dict()
#             if 'html' in request_data:
#                 return render_template(
#                     'temp_markdown.html',
#                     title1='mySync',
#                     title2='MD',
#                     markdownstr=markdownstr[1:-1])
#             else:
#                 return markdownstr

#         elif access_method == 'POST':
#             request_data = request.form.to_dict()
#             if 'mdcon' in request_data:
#                 filefd.write_cover(jsondecode(request_data['mdcon']))
#                 return 'success'
#             else:
#                 return 'get wrong data'

#         elif access_method == 'DELETE':
#             # TODO
#             return abort(405)

#         else:  # end if method
#             return abort(405)
