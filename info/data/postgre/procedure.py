from . import execute, query, conf


def get_requests(*args, **kwargs):
    ans = execute(query.get_requests, *args, **kwargs)
    if ans == 0:
        ans = "[]"
    return ans


def count_requests(*args, **kwargs):
    ans = execute(query.count_requests, *args, **kwargs)
    # print("!!!!", ans)
    return ans["count"]


def get_query_requests(*args, **kwargs):
    ans = execute(query.get_query_requests, *args, **kwargs)
    if ans == 0:
        ans = "[]"
    return ans


def count_query_requests(*args, **kwargs):
    ans = execute(query.count_query_requests, *args, **kwargs)
    # print("!!!!", ans)
    return ans["count"]


def create_row_request(*args, **kwargs):
    ans = execute(query.create_row_request, *args, array=False, to_json=False, to_commit=True)
    try:
        ans = None if ans == 0 else dict(ans)["id"]     # TODO нормально обработать ошибку
    except:
        return ans
    return ans


def create_row_response(*args, **kwargs):
    ans = execute(query.create_row_response, *args, array=False, to_json=False, to_commit=True)
    try:
        ans = None if ans == 0 else dict(ans)["id"]     # TODO нормально обработать ошибку
    except:
        return ans
    return ans


def check_subscribe(*args, **kwargs):
    ans = execute(query.check_subscribe, *args, **kwargs)
    return ans


def nmb_request_inc(*args, **kwargs):
    ans = execute(query.nmb_request_inc, *args, **kwargs)
    return ans


def get_request_summary(*args, **kwargs):
    ans = execute(query.get_request_summary, *args, **kwargs, to_json=False)
    if isinstance(ans, int): return ans
    bea_ans = {"queryset": ans[0]["queryset"], "dttm": ans[0]["dttm_open"], "r_status": ans[0]["r_status"],
               "response": {}}
    for el in ans:
        bea_ans["response"][el["resource_id"]] = {"name": el["name"], "status": el["status"],
                                                  "information": el["response"]}
    return bea_ans


def get_report_info(*args, **kwargs):
    ans = execute(query.get_report_info, *args, **kwargs, array=False, to_json=False)
    if isinstance(ans, int):
        if ans == 0: return "Not found", 404
        if ans < 0: return "server error", 500
    return ans["status"], 200   #Attention! status "not found" may be have code 200 or 404 - it's different answer!
