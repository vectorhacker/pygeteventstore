# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='geteventstore',
    version='0.0.1',
    description='Python Implementation of the EventStore API client',
    long_description=readme,
    author='Victor A Martinez',
    author_email='victor@plazsa.com',
    url='https://github.com/vectorhacker/pygeteventstore',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
