# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

license = ''

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='geteventstore',
    version='0.0.1',
    description='Python HTTP Client for the Event Store API',
    long_description=readme,
    author='Victor A. Martinez Santiago',
    author_email='victor@plazsa.com',
    url='https://github.com/vectorhacker/pygeteventstore',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

