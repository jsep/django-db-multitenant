#!/usr/bin/env python

from os.path import exists

from setuptools import setup, find_packages

README = 'README.rst'

setup(
    name='django-db-multitenant',
    version='0.2.0',
    author='mike wakerly',
    author_email='opensource@hoho.com',
    packages=find_packages(),
    url='https://github.com/mik3y/django-db-multitenant',
    license='BSD',
    description='Multitenant support for Django, using one tenant per database.',
    long_description=open(README).read() if exists(README) else "",
    install_requires=[
        'Django >= 1.8.0',
    ],
)
