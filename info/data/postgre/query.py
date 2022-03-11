get_requests = """
            SELECT id, queryset, status, to_char(dttm_open, 'DD.MM.YYYY') as dttm
            FROM requests
            WHERE user_id=%(user_id)s
            ORDER BY id DESC
            LIMIT %(limit)s
            OFFSET %(offset)s
            """


count_requests = """
                select count(*)
                from requests
                where user_id=%(user_id)s;
                """


get_query_requests = """
            SELECT id, queryset, status, to_char(dttm_open, 'DD.MM.YYYY') as dttm
            FROM requests
            WHERE user_id=%(user_id)s AND lower(queryset->>'sname') = %(sname)s
            ORDER BY id DESC;
            """


count_query_requests = """
                select count(*)
                from requests
                where user_id=%(user_id)s AND lower(queryset->>'sname') = %(sname)s
                ;
                """


create_row_request = """
             INSERT INTO requests (user_id, queryset, status, dttm_open, dttm_last)
             VALUES (%(user_id)s, %(queryset)s, %(status)s, %(dttm_open)s, %(dttm_last)s)
             RETURNING id;
            """


create_row_response = """
             INSERT INTO responses (request_id, resource_id, status)
             VALUES (%(request_id)s, %(resource_id)s, %(status)s)
             RETURNING id;
            """


check_subscribe = """
            SELECT nmb_request, date_access::date, level_access 
            FROM userinfo
            WHERE user_id=%(user_id)s
            """

nmb_request_inc = """
            UPDATE userinfo SET nmb_request=nmb_request-1 WHERE user_id=%(user_id)s
            """

get_request_summary = """
            SELECT t.*, t2.name FROM
                (select r2.*, r.response, r.status, r.resource_id from responses r 
                join (SELECT id, queryset, status as r_status, dttm_open 
                        FROM requests WHERE id=%(id_request)s and user_id=%(user_id)s) r2 
                ON r.request_id=r2.id) t
            JOIN resources t2
            ON t.resource_id=t2.id;
"""


get_report_info = """
            SELECT * FROM requests
            WHERE user_id=%(user_id)s AND id=%(file_id)s;
"""
