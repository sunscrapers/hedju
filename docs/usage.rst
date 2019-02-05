=====
Usage
=====

To use REST Header Pagination in a project, choose your preferred pagination
style (see below). Each time you will have ``envelope`` param available.
If you set it to true (or 1), you'll get original behavior of respective
DRF's class but the Headers will also be set.

HeaderPageNumberPagination
===========================

Request::
    GET https://api.example.com/accounts/?page=2

Response::

    HTTP 200 OK

    Headers:
        Link: <https://api.example.com/accounts/>; rel="first", <https://api.example.com/accounts/?page=1>; rel="prev", <https://api.example.com/accounts/?page=3>; rel="next", <https://api.example.com/accounts/?page=9>; rel="last"

    Body:
    [
        {
            "id": 1,
            "name": "John Doe",
        },
        ...
    ]


Request::
    GET https://api.example.com/accounts/?page=2&envelope=true

Response::

    HTTP 200 OK

    Headers:
        Link: <https://api.example.com/accounts/?envelope=true>; rel="first", <https://api.example.com/accounts/?page=1>; rel="prev", <https://api.example.com/accounts/?page=3>; rel="next", <https://api.example.com/accounts/?page=9>; rel="last"

    Body:

    {
        "count": 882,
        "first": "https://api.example.com/accounts/?envelope=true",
        "previous": "https://api.example.com/accounts/?page=1&envelope=true",
        "next": "https://api.example.com/accounts/?page=3&envelope=true",
        "last": "https://api.example.com/accounts/?page=9&envelope=true",
        "results": [
            {
                "id": 1,
                "name": "John Doe",
            },
            ...
        ]
    }

Setup
-----

To enable the LimitOffsetPagination style globally, use the following configuration::

    REST_FRAMEWORK = {
        ...
        'DEFAULT_PAGINATION_CLASS': 'hedju.HeaderPageNumberPagination',
        'PAGE_SIZE': 100,
    }


HeaderLimitOffsetPagination
===========================

Request::
    GET https://api.example.com/accounts/?limit=100&offset400

Response::

    HTTP 200 OK

    Headers:
        Link: <https://api.example.com/accounts/?limit=100>; rel="first", <https://api.example.com/accounts/?limit=100&offset=300>; rel="prev", <https://api.example.com/accounts/?limit=100&offset=500>; rel="next", <https://api.example.com/accounts/?limit=100&offset=782>; rel="last"

    Body:
    [
        {
            "id": 1,
            "name": "John Doe",
        },
        ...
    ]


Request::
    GET https://api.example.com/accounts/?limit=100&offset400&envelope=true

Response::

    HTTP 200 OK

    Headers:
        Link: <https://api.example.com/accounts/?limit=100&envelope=true>; rel="first", <https://api.example.com/accounts/?limit=100&offset=300&envelope=true>; rel="previous", <https://api.example.com/accounts/?limit=100&offset=500&envelope=true>; rel="next", <https://api.example.com/accounts/?limit=100&offset=782&envelope=true>; rel="last"

    Body:

    {
        "count": 882,
        "first": "https://api.example.com/accounts/?limit=100&envelope=true",
        "previous": "https://api.example.com/accounts/?limit=100&offset=300&envelope=true",
        "next": "https://api.example.com/accounts/?limit=100&offset=500&envelope=true",
        "last": "https://api.example.com/accounts/?limit=100&offset=782&envelope=true",
        "results": [
            {
                "id": 1,
                "name": "John Doe",
            },
            ...
        ]
    }

Setup
-----

To enable the LimitOffsetPagination style globally, use the following configuration::

    REST_FRAMEWORK = {
        ...
        'DEFAULT_PAGINATION_CLASS': 'hedju.HeaderLimitOffsetPagination',
        'PAGE_SIZE': 100,  # Optional
    }

