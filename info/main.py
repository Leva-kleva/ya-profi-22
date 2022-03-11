from functools import wraps

from flask import Flask, request, make_response, g
import json
import requests as rq
from datetime import datetime
from datetime import date as DATE
from data import postgre
import conf

app = Flask(__name__)
app.config['SECRET_KEY'] = conf.secret_key


def template_response(body, code, is_json=False):
    if not is_json:
        status = "info" if code < 400 else "error"
        tmp = f'{{"{status}": "{body}"}}'
        body = tmp
    response = make_response(body, code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.before_request
def check_access():
    try:
        headers = dict(request.headers)
        headers['Content-Length'] = '0'
        response = rq.get(conf.url_auth, headers=headers)
    except:
        return template_response("Server error", 500)
    if response.status_code >= 400:
        return template_response(response.json(), response.status_code, is_json=True)
    g.user = response.json()


roles = {
    'user': 0,
    'admin': 1,
    'superuser': 2,
}


def check_role(role):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            user_role_number = g.user.get('role')
            if user_role_number is not None and user_role_number < roles[role]:
                return template_response("Нет доступа", 403)
            return f(*args, **kwargs)

        return wrapped

    return decorator



@app.route('/search', methods=["POST"])
@check_role('user')
def search_post():
    type = request.json.pop('type').strip()
    uri = request.json.pop('url').strip()
    if type == "csv1": pass ## обработка локальных файлов csv xls
    if type == "csv2": pass  ## обработка сетевых файлов csv xls
    if type == "pg": pass  ## обработка postgre-таблицы uri
    if type == "mg": pass  ## обработка mg-таблицы uri
    return template_response("OK", 201, is_json=False)


if __name__ == '__main__':
    app.run(debug=conf.debug, port=conf.port, host=conf.host)

