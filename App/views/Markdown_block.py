from flask import Blueprint, request, abort
from flask import render_template
from json import dumps as jsonencode
from json import loads as jsondecode
from os import listdir

from werkzeug.utils import secure_filename

from App.ext import FileConCtrl

Markdown_block = Blueprint('Markdown_block', __name__)


@Markdown_block.route('/markdown')
def test():
    return render_template('index_markdown.html', title1='mySync', title2='MD')


@Markdown_block.route(
    '/v<float:version>/Markdown',
    methods=['GET', 'POST', 'DELETE'])
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
            try:
                markdown_list = jsonencode(listdir('data/markdown'))
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


@Markdown_block.route(
    '/v<float:version>/Markdown/<resid_raw>',
    methods=['GET', 'POST', 'DELETE'])
def get_put_path_res_by_id(version, resid_raw):
    access_method = request.method
    mdfilename = secure_filename(resid_raw)
    filefd = FileConCtrl('data/markdown/' + mdfilename)
    markdownstr = ''

    if version == 1.0:
        return abort(410)
    elif version == 2.0:
        return abort(410)

    # ------------------------------------------
    #   @uri: http://host:port/v2.1/markdown/test.md
    #   @methods: GET POST DELETE
    # ------------------------------------------
    elif version == 2.1:

        if access_method == 'GET':

            try:  # read markdown data from file
                markdownstr = jsonencode(filefd.read())
                # print(markdownstr)
            except Exception as err:
                print(err)
                abort(404)

            request_data = request.args.to_dict()
            if 'html' in request_data:
                return render_template(
                    'temp_markdown.html',
                    title1='mySync',
                    title2='MD',
                    markdownstr=markdownstr[1:-1])
            else:
                return markdownstr

        elif access_method == 'POST':
            request_data = request.form.to_dict()
            if 'mdcon' in request_data:
                filefd.write_cover(jsondecode(request_data['mdcon']))
                return 'success'
            else:
                return 'get wrong data'

        elif access_method == 'DELETE':
            # TODO
            return abort(405)

        else:  # end if method
            return abort(405)
