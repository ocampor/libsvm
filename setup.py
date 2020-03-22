import os
import sys
from setuptools import setup
from distutils.extension import Extension

import libsvm

DESCRIPTION = 'Pre-built LibSVM packages for Python.'
LICENSE = 'Apache 2.0'
DIST_NAME = 'libsvm'
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
AUTHOR_EMAIL = 'me@ocampor.ai'
AUTHOR = 'Ricardo Ocampo'
URL = 'https://github.com/ocampor/libsvm'
VERSION = libsvm.__version__

with open(os.path.join(ROOT_PATH, 'README.rst'), 'r', encoding="utf-8") as readme:
    LONG_DESCRIPTION = readme.read()

if sys.platform == 'win32':
    EXT_MODULES = []
else:
    libsvm = Extension(
        'libsvm',
        sources=['src/libsvm/svm.cpp'])
    EXT_MODULES = [libsvm]

setup(
    name=DIST_NAME,
    packages=['libsvm'],
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    extras_require={
        'dev': [
            'pytest',
            'pytest-pep8',
            'pytest-cov'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data=True,
    python_requires=">=3.5",
    ext_modules=EXT_MODULES)
