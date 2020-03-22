.. -*- mode: rst -*-

|Travis|_ |PyPi|_

.. |Travis| image:: https://travis-ci.com/ocampor/libsvm.svg?branch=master
.. _Travis: https://travis-ci.com/ocampor/libsvm

.. |PyPi| image:: https://img.shields.io/pypi/dm/libsvm?color=blue   :alt: PyPI - Downloads
.. _PyPi: https://pypi.org/project/libsvm/

LibSVM
======

Description
-----------

Pre-built LibSVM packages for Python.

What is LibSVM?
---------------

Crated by Chih-Chung Chang and Chih-Jen Lin, LIBSVM is an integrated
software for support vector classification, (C-SVC, nu-SVC), regression
(epsilon-SVR, nu-SVR) and distribution estimation (one-class SVM). It
supports multi-class classification.

Original Links
--------------

-  Repository: https://github.com/cjlin1/libsvm
-  Library website: https://www.csie.ntu.edu.tw/~cjlin/libsvm

Purpose of this package
-----------------------

The idea behind this package is to use the same code as in
https://github.com/cjlin1/libsvm using the very convenient pip command

How to install
--------------

::

   pip install libsvm

Example
-------

1. Download https://github.com/cjlin1/libsvm/blob/master/heart_scale
   file.
2. Run the following commands

::

   >>> from libsvm.svmutil import *
   >>> y, x = svm_read_problem('path/to/heart_scale')
   >>> m = svm_train(y[:200], x[:200], '-c 4')
   *.*
   optimization finished, #iter = 257
   nu = 0.351161
   obj = -225.628984, rho = 0.636110
   nSV = 91, nBSV = 49
   Total nSV = 91
   >>> p_label, p_acc, p_val = svm_predict(y[200:], x[200:], m)
   Accuracy = 84.2857% (59/70) (classification)

Windows
-------

The package contains a pre-built Windows binary that is only compatible with 64 bits architecture; therefore,
32 bits architecture is not compatible.

Cygwin
______

In case that you want to install this package using Cygwin, you have to make sure that the
following packages are installed:

1. gcc-g++ >= 7.0.0
2. python38
3. python38-devel
4. python38-pip

Some good tutorials to install Cygwin packages are the following:

- https://wiki.usask.ca/display/MESH/Running+Python+from+the+Cygwin+Terminal
- https://www.davidbaumgold.com/tutorials/set-up-python-windows/#installing-cygwin

Copyright
---------

Copyright (c) 2000-2018 Chih-Chung Chang and Chih-Jen Lin All rights
reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither name of copyright holders nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Maintainer
----------

-  Ricardo Ocampo `me@ocampor.ai`_

.. _me@ocampor.ai: me@ocampor.ai
