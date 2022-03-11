from . import Get, conf


def get_requests(request):
    obj = Get(conf.url_info + "/requests", request)
    obj.make_full_request()
    return obj.response.json()


def get_request_summary(request, id_request):
    obj = Get(conf.url_info + f"/requests/{id_request}", request)
    obj.make_full_request()
    return obj.response.json()
