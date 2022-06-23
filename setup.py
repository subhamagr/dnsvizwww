#!/usr/bin/env python

import glob
import os
import sys

from distutils.core import setup


with open("requirements.txt", "r") as req_file:
    requirements = tuple(req_file)

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name='dnsvizwww',
    version='0.2.0pre',
    author='Casey Deccio',
    author_email='casey@deccio.net',
    url='https://github.com/dnsviz/dnsvizwww/',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    description='DNS analysis and visualization tool suite - Web and database components',
    long_description=readme,
    license='LICENSE',
    scripts=['bin/dnsget-db', 'bin/dnsviz-db', 'bin/dnsgrok-db'],
    packages=['dnsvizwww'],
    install_requires=requirements,
    setup_requires=[],
    test_suite="tests",
    tests_require=[],
    include_package_data=True,
    data_files=[
        ('share/doc/dnsvizwww', ['README', 'LICENSE']),
        ('share/dnsvizwww/static/css', glob.glob(os.path.join('dnsvizwww', 'static', 'css', '*.css'))),
        ('share/dnsvizwww/static/css/redmond', ['dnsvizwww/static/css/redmond/jquery-ui-1.10.4.custom.min.css']),
        ('share/dnsvizwww/static/css/redmond/images', glob.glob(os.path.join('dnsvizwww', 'static', 'css', 'redmond', 'images', '*.png')) + glob.glob(os.path.join('dnsvizwww', 'static', 'css', 'redmond', 'images', '*.gif'))),
        ('share/dnsvizwww/static/images', glob.glob(os.path.join('dnsvizwww', 'static', 'images', '*.png')) + glob.glob(os.path.join('dnsvizwww', 'static', 'images', '*.gif'))),
        ('share/dnsvizwww/static/images', ['dnsvizwww/static/images/favicon.ico']),
        ('share/dnsvizwww/static/images/dnssec_legend', glob.glob(os.path.join('dnsvizwww', 'static', 'images', 'dnssec_legend', '*.png'))),
        ('share/dnsvizwww/static/js', glob.glob(os.path.join('dnsvizwww', 'static', 'js', '*.js'))),
        ('share/dnsvizwww/templates', glob.glob(os.path.join('dnsvizwww', 'templates', '*.html'))),
    ],
)
