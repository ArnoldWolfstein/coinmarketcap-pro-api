#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from coinmarketcap import __version__

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name='coinmarketcap-pro-api',
    version=__version__,
    author='Jiawei Xu',
    author_email='contactxjw@gmail.com',
    url='https://github.com/xjw0914/coinmarketcap-pro-api',
    packages=['coinmarketcap'],
    description='Python wrapper for CoinMarketCap Professional API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_required=['requests'],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
