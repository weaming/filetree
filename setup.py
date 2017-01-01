#!/usr/bin/env python
# coding: utf-8

import re
from setuptools import setup, find_packages

with open('filetree/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name = "filetree",
    version = version,
    description = 'Easier file tree.',
    long_description = open('README.rst', 'r').read(),
    author = 'weaming',
    author_email = 'garden.yuen@gmail.com',
    url = 'https://github.com/weaming/filetree',
    license = 'MIT',
    keywords = 'file tree fs',
    packages = find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires = ['ordereddict'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
