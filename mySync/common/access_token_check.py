from functools import wraps

from flask import request, abort

from mySync.config.settings import settings


def check_access_token(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "access_token" not in request.headers:
            return abort(401)
        if request.headers.get("access_token") != settings.ACCESS_TOKEN:
            return abort(401)

        return func(*args, **kwargs)

    return wrapper
