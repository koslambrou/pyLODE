#!/usr/bin/env python
# -*- coding: latin-1 -*-
import codecs
import re
import os
from setuptools import setup

def open_local(paths, mode='r', encoding='utf8'):
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        *paths
    )
    return codecs.open(path, mode, encoding)

with open_local(['pylode', '__init__.py'], encoding='latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

with open_local(['README.rst'], encoding='utf-8') as readme:
    long_description = readme.read()

with open_local(['requirements.txt']) as req:
    install_requires = req.read().split("\n")

setup(
    name='pyLODE',
    packages=['pylode'],
    package_dir={'pylode': 'pylode'},
    package_data={'pylode': ['templates/*.html', 'templates/*.md', 'style/*.css']},
    version=version,
    description='An OWL ontology documentation tool using Python and templating, based on LODE.',
    author='Nicholas Car',
    author_email='nicholas.car@surroundaustralia.com',
    url='https://github.com/rdflib/pyLODE',
    download_url='https://github.com/rdflib/pyLODE/archive/v{:s}.tar.gz'.format(version),
    license='LICENSE',
    keywords=['Semantic Web', 'OWL', 'ontology', 'template', 'Jinja2', 'documentation'],
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'pylode = pylode.cli:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/rdflib/pyLODE/issues',
        'Source': 'https://github.com/rdflib/pyLODE/',
    },
    install_requires=install_requires,
)
