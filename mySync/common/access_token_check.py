from functools import wraps

from flask import request, abort

from mySync.config.settings import settings
from hmac import compare_digest


def check_access_token(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = str(request.headers.get("access_token", "none"))
        print(token)
        if not compare_digest(token, settings.ACCESS_TOKEN):
            return abort(401)

        return func(*args, **kwargs)

    return wrapper
