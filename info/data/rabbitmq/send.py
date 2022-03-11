from . import *


def search_man(queryset):
    ans = send_execute(queue='search_man', exchange='', body=queryset)
    return ans


def general_info(queryset):
    ans = send_execute(queue='general_infoo', exchange='', body=queryset)
    return ans


def general_negative(queryset):
    ans = send_execute(queue='general_negative', exchange='', body=queryset)
    return ans


def fssp_debt(queryset):
    ans = send_execute(queue='fssp_debt', exchange='', body=queryset)
    return ans


def fns_disq(queryset):
    ans = send_execute(queue='fns_disq', exchange='', body=queryset)
    return ans


def federal_search(queryset):
    ans = send_execute(queue='federal_search', exchange='', body=queryset)
    return ans


def fsin_search(queryset):
    ans = send_execute(queue='fsin_search', exchange='', body=queryset)
    return ans


def terrorists_search(queryset):
    ans = send_execute(queue='terrorists_search', exchange='', body=queryset)
    return ans


def check_passport(queryset):
    ans = send_execute(queue='check_passport', exchange='', body=queryset)
    return ans


def check_snils(queryset):
    ans = send_execute(queue='check_snils', exchange='', body=queryset)
    return ans


def fns_debt(queryset):
    ans = send_execute(queue='fns_debt', exchange='', body=queryset)
    return ans
