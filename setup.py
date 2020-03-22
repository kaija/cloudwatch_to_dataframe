#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of cloudwatch-to-dataframe.
# https://github.com/kaija/cloudwatch_to_dataframe

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2020, kaija <kaija.chang@gmail.com>

from setuptools import setup, find_packages
from cloudwatch_to_dataframe import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='cloudwatch-to-dataframe',
    version=__version__,
    description='convert cloudwatch metrics to dataframe',
    long_description='''
convert cloudwatch metrics to dataframe
''',
    keywords='cloudwatch, dataframe',
    author='kaija',
    author_email='kaija.chang@gmail.com',
    url='https://github.com/kaija/cloudwatch_to_dataframe',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'cloudwatch-to-dataframe=cloudwatch_to_dataframe.cli:main',
        ],
    },
)
