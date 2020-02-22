from flask import Blueprint

from mySync.config import settings

from json import dumps as jsonencode

VisitCounter_routes = Blueprint('VisitCounter_routes', __name__)

VISITCOUNTER_TABLENAME = settings.VISITCOUNTER_TABLENAME


@VisitCounter_routes.route('/VisitCounter/<path:routes>')
def visit_counter(routes):
    # print(routes)
    print(routes.split('/'))
    return routes


def addCount(path):
    # addcount

    return path