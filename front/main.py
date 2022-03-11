from flask import Flask, redirect, url_for, request, render_template, g, send_file, make_response
from werkzeug.exceptions import abort
import os

import conf
import pageinfo

app = Flask(__name__)
app.config['SECRET_KEY'] = conf.secret_key

roles = {
    'user': 0,
    'admin': 1,
    'superuser': 2,
}


def check_role(role):
    def decorator(func):
        def wrapped(*args, **kwargs):
            user_role_number = g.user.get('role')
            if user_role_number is not None and user_role_number < roles[role]:
                return abort(403)
            return func(*args, **kwargs)

        wrapped.__name__ = func.__name__
        return wrapped

    return decorator


@app.before_request
def check_access():
    if request.endpoint in ("index", "static"): return
    obj = pageinfo.Get(conf.url_auth, request)
    obj.make_request()
    if obj.response.status_code == 401:
        if request.endpoint in ("login",):
            g.user = None
            return
        return redirect(url_for('login'))
    elif obj.response.status_code >= 400:
        return abort(obj.response.status_code)
    else:
        g.user = obj.response.json()


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return redirect(url_for('login'))
    # return render_template("index/index.html")


@app.route('/login', methods=['GET'])
def login():
    # if g.user is not None:
    #     return redirect(url_for('account_search'))
    return render_template("auth/login.html")


@app.route('/account/search', methods=['GET'])
def account_search():
    return render_template("account/search_form.html")


@app.route('/account/requests', methods=['GET'])
def account_requests():
    pagination = pageinfo.info.get_requests(request)
    return render_template("account/requests.html", pagination=pagination)


if __name__ == '__main__':
    app.run(debug=conf.debug, port=conf.port, host=conf.host)
