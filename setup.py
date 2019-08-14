import os
from distutils.core import setup
from distutils.extension import Extension

import libsvm

DESCRIPTION = 'Python package for libsvm package'
LICENSE = 'Apache 2.0'
DIST_NAME = 'libsvm'
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
AUTHOR_EMAIL = 'me@ocampor.ai'
AUTHOR = 'Ricardo Ocampo'
URL = 'https://github.com/ocampor/libsvm'
VERSION = libsvm.__version__

libsvm = Extension(
    'libsvm',
    sources=['src/libsvm/svm.cpp'])

setup(
    name=DIST_NAME,
    packages=['libsvm'],
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=[
        'scipy>=1.3.0',
    ],
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
    python_requires=">=3.7",
    ext_modules=[libsvm])
