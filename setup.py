#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='linefeeder',
    version='0.0.3',
    description='feed bytes and get lines',
    author='Tomotaka Ito',
    author_email='tomotaka.ito@gmail.com',
    url='https://github.com/tomotaka/linefeeder',
    packages=find_packages(),
    license=open('LICENSE').read(),
    include_package_data=True,
    # install_requires=[],
    tests_require=['nose'],
    test_suite='nose.collector'
)
