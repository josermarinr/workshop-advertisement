#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name='blueprint-webapp-flask-graphql',
    version='1.0.0',
    packages=find_packages(exclude=["*_tests"]),
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
        'ariadne',
        'flask',
        'flask-cors',
        'gunicorn'
    ],
    extras_require={
        'dev': [
            'honcho',
            'pylint',
            'coverage'
        ]
    },
    classifier=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'Operating System :: POSIX :: Linux'
    ],
    python_requires='~=3.6',
)
