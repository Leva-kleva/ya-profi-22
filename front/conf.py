import os

debug = os.environ.get('DEBUG') if os.environ.get('DEBUG') else True
if debug == "False":
    debug = False

host = "0.0.0.0"
port = os.environ.get('FRONT_PORT') if os.environ.get('FRONT_PORT') else 5010
server_user = os.environ.get('SERVER_USER') if os.environ.get('SERVER_USER') else "a"

secret_key = os.environ.get('SECRET_KEY') if os.environ.get('SECRET_KEY') else "secret"

auth_host = os.environ.get('AUTH_HOST') if os.environ.get('AUTH_HOST') else "localhost"
auth_port = os.environ.get('AUTH_PORT') if os.environ.get('AUTH_PORT') else 5002

info_host = os.environ.get('INFO_HOST') if os.environ.get('INFO_HOST') else "localhost"
info_port = os.environ.get('INFO_PORT') if os.environ.get('INFO_PORT') else 5001

if debug:
    url_auth = "http://localhost/api/v1/login"
    url_info = "http://localhost/api/v1/info"
else:
    url_auth = "http://{0}:8000/login".format(auth_host)
    url_info = "http://{0}:8000".format(info_host)
