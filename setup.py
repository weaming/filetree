#!/usr/bin/python
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
    long_description = open('README.md', 'r').read(),
    author = 'weaming',
    author_email = 'garden.yuen@gmail.com',
    url = 'https://github.com/weaming/filetree',
    license = 'MIT',
    packages = find_packages(),
    setup_requires=[],
    test_suite=None,
)
