# -*- coding: utf-8 -*-

"""Top-level package for REST Header Pagination."""

__author__ = """Sunscrapers"""
__email__ = 'd.kozaczko@sunscrapers.com'
__version__ = '0.1.0'

import sys

if 'sphinx' not in sys.modules:
    from .pagination import *  # noqa
