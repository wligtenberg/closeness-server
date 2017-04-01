# -*- coding: utf-8 -*-
# closeness-server (c) Willem Ligtenberg

import re
import os
import codecs
from setuptools import setup, find_packages
from distutils.dir_util import copy_tree


def read(*rnames):
    return codecs.open(os.path.join(os.path.dirname(__file__), *rnames), 'r', 'utf-8').read()


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, read('closeness_server/__meta__.py'))
    return strval


setup(
    version=grep('__version__'),
    name='closeness-server',
    description="Server to store the closeness data",
    packages=find_packages(),
    scripts=[
        "bin/runserver.py",
        "bin/manage.py",
    ],
    long_description=read('Readme.rst'),
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    url=grep('__url__'),
    install_requires=read('requirements.txt'),
    license='MIT',
    zip_safe=False,
)
