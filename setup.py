#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pip.req import parse_requirements

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "scipy",
    "numpy"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='complexityfinder',
    version='0.22.37',
    description="complexityFinder helps you find computational complexity of your function",
    long_description=readme + '\n\n' + history,
    author="Bartosz Radzyński",
    author_email='radzynskib@gmail.com',
    url='https://github.com/bartosz822/complexityfinder',
    packages=[
        'complexityfinder',
    ],
    package_dir={'complexityfinder':
                 'complexityfinder'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='complexityfinder',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
