import json

from flask import Flask, request, make_response, abort, session
import data
import schemes
import conf
from hashlib import sha256

app = Flask(__name__)
app.config['SECRET_KEY'] = conf.secret_key
app.secret_key = conf.secret_key

refresh_list = set()


def template_response(body, code, is_json=False):
    if not is_json:
        status = "info" if code < 400 else "error"
        tmp = f'{{"{status}": "{body}"}}'
        body = tmp
    response = make_response(body, code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route('/login', methods=['GET'])
def is_auth():
    if 'user_id' in session and 'role' in session and session["user_id"] not in refresh_list:
        body = json.dumps({"user_id": session["user_id"], "role": session["role"]})
        return template_response(body, 200, is_json=True)
    return template_response("Пользователь не авторизован", 401)


@app.route('/login', methods=['POST'])
def login_post():
    if not schemes.check(request, schemes.login.post):
        return template_response('Невалидный запрос', 400)

    login = request.json['login'].strip()
    password = sha256(request.json['password'].encode()).hexdigest()

    ans = data.procedure.get_user({"password": password, "login": login}, array=False, to_json=False)

    body, code = data.check_errors(ans, body="OK", code=202)

    if code < 400:
        if ans["id"] in refresh_list:
            refresh_list.remove(ans["id"])
        session["user_id"] = ans["id"]
        session["role"] = ans["role"]

    return template_response(body, code)


@app.route('/login', methods=["PUT"])
def refresh():
    if session["role"] < 1:
        return template_response("Запрещено", 403)
    user_id = int(request.args.get('user_id'))
    # if 'user_id' not in session and 'role' not in session:
    #     return template_response('Пользователь не авторизован', 401)
    refresh_list.add(user_id)
    return template_response('OK', 200)


@app.route('/login', methods=["DELETE"])
def logout():
    if 'user_id' in session and 'role' in session:
        session.clear()
        return template_response('OK', 200)
    return template_response('Пользователь не авторизован', 401)


if __name__ == '__main__':
    app.run(debug=conf.debug, port=conf.port, host=conf.host)
