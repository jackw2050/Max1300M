# -*- coding: utf-8 -*-

try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name                = 'MAX1300M',
    version             = '0.1.0',
    description         = 'Beaglbone Black Python library for MAX1300 ADC',
    long_description    = readme,
    author_email        = 'Jack Walker',
    author_email        = 'zls.jackwalker@zlscorp.com',
    url                 = 'https://github.com/jackw2050/Max1300M',
    license             = license,
    classifiers         = classifiers,
    dependency_links    = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
    install_requires    = ['Adafruit-GPIO>=0.6.5'],
    find_packages       = find_packages(exclude=('tests', 'docs'))
)


