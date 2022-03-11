from . import Get, conf


def get_user(request):
    obj = Get(conf.url_account, request)
    obj.make_full_request()
    return obj.response.json()


def get_messages(request):
    obj = Get(conf.url_account + "/support", request)
    obj.make_full_request()
    return obj.response.json()
