#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner',]

test_requirements = [
    'django>=1.11,<2.3',
    'djangorestframework>=3.8',
    'factory_boy==2.11.1',
    'pytest',
    'pytest-django==3.4.7',
]

setup(
    author="Sunscrapers",
    author_email='d.kozaczko@sunscrapers.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Class implementing limit/offset pagination in headers with optional enveloping.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='hedju',
    name='hedju',
    packages=find_packages(include=['hedju']),
    setup_requires=setup_requirements,
    test_suite='testproject',
    tests_require=test_requirements,
    url='https://github.com/sunscrapers/hedju',
    version='0.1.0',
    zip_safe=False,
)
