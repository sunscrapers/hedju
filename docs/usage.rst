=====
Usage
=====

To use REST Header Pagination in a project, put this in your ``settings.py`` ::

    REST_FRAMEWORK = {
        ...
        'DEFAULT_PAGINATION_CLASS': 'hedju.HeaderLimitOffsetPagination',

    }
