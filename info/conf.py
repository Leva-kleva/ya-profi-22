import os

pg_database = os.environ.get('DB_NAME') if os.environ.get('DB_NAME') else 'a'
pg_login = os.environ.get('DB_LOGIN') if os.environ.get('DB_LOGIN') else 'a'
pg_password = os.environ.get('DB_PASSWORD') if os.environ.get('DB_PASSWORD') else 'a'
pg_host = os.environ.get('DB_HOST') if os.environ.get('DB_HOST') else 'localhost'
pg_port = os.environ.get('DB_PORT') if os.environ.get('DB_PORT') else 5432

rbt_host = os.environ.get('RABBITMQ_HOST') if os.environ.get('RABBITMQ_HOST') else 'localhost'
rbt_port = os.environ.get('RABBITMQ_PORT') if os.environ.get('RABBITMQ_PORT') else 5672

debug = os.environ.get('DEBUG') if os.environ.get('DEBUG') else True
if debug == "False":
    debug = False

host = "0.0.0.0"
port = os.environ.get('INFO_PORT') if os.environ.get('INFO_PORT') else 5001

secret_key = os.environ.get('SECRET_KEY') if os.environ.get('SECRET_KEY') else "secret"

auth_host = os.environ.get('AUTH_HOST') if os.environ.get('AUTH_HOST') else "localhost"
auth_port = os.environ.get('AUTH_PORT') if os.environ.get('AUTH_PORT') else 5002

if debug:
    url_auth = "http://localhost/api/v1/login"
else:
    url_auth = "http://{0}:8000/login".format(auth_host)

page_size = 20
nmb_pages = 4