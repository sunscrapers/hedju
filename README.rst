===================================================
Hedju - Header Pagination for Django REST Framework
===================================================


.. image:: https://img.shields.io/pypi/v/hedju.svg
        :target: https://pypi.python.org/pypi/hedju

.. image:: https://img.shields.io/travis/sunscrapers/hedju.svg
        :target: https://travis-ci.org/sunscrapers/hedju

.. image:: https://readthedocs.org/projects/hedju/badge/?version=latest
        :target: https://hedju.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Replacement for Django REST Framework's pagination classes implementing
Link header as defined in RFC5988_ with optional enveloping.

Inspired by `this paragraph from excellent article<https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api#pagination>`_ by Vinay Sahni

.. note:: This is pre-alpha code. Use at your own discretion.

* Free software: MIT license
* Documentation: https://hedju.readthedocs.io.


Features
--------

* Provides ``first``, ``prev``, ``next`` and ``last`` links via headers.
* Optional enveloping for clients without header support - returns structure
  compatible with original class but with extra ``first`` and ``last`` links.


Credits
-------

Developed by SUNSCRAPERS_ with passion & patience.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _SUNSCRAPERS: https://sunscrapers.com/
.. _RFC5988: http://tools.ietf.org/html/rfc5988#page-6
