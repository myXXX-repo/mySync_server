from flask import Blueprint, abort

app_temp_routes = Blueprint('app_temp_routes', __name__)


@app_temp_routes.route('/app/tmp')
def app_tmp():
    return abort(404)
