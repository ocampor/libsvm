import os
from distutils.core import setup
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

with open(os.path.join(ROOT_PATH, 'README.rst'), 'r') as readme:
    LONG_DESCRIPTION = readme.read()

libsvm = Extension(
    'libsvm',
    sources=['src/libsvm/svm.cpp'])

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
    python_requires=">=3.4",
    ext_modules=[libsvm])
