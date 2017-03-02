# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MAX1300M',
    version='0.1.0',
    description='Beaglbone Black Python library for MAX1300 ADC',
    long_description=readme,
    author='Jack Walker',
    author_email='zls.jackwalker@zlscorp.com',
    url='https://github.com/jackw2050/Max1300M',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

