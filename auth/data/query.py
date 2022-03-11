get_user = "SELECT * FROM users WHERE login=lower(%(login)s) and password=%(password)s and is_active=true;"

get_user_by_id = "SELECT * FROM users WHERE id=%(user_id)s"
