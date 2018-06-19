#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['oceandb-driver-interface==0.1.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="OceanProtocol",
    author_email='enrique@oceanprotocol.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='oceandb-mongo-driver',
    name='oceandb-mongo-driver',
    packages=find_packages(include=['oceandb-mongo-driver']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/oceanprotocol/oceandb-mongo-driver',
    version='0.1.0',
    zip_safe=False,
)
