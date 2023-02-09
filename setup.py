###############################################################################
#
# Copyright (c) 2007 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for z3c.traverser package
"""
import os.path

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    data = open(os.path.join(os.path.dirname(__file__), *rnames)).read()
    return data + "\n\n"


TESTS_REQUIRE = [
    'WebTest',
    'zope.app.appsetup',
    'zope.app.publication',
    'zope.app.wsgi >= 4.0.0a4',
    'zope.authentication',
    'zope.browserpage',
    'zope.container',
    'zope.error',
    'zope.principalregistry',
    'zope.security',
    'zope.site',
    'zope.testbrowser',
    'zope.testing',
    'zope.testrunner>=4.3.1',
]

setup(name='z3c.traverser',
      version='2.0',
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.dev',
      description='Pluggable Traversers And URL handling utilities',
      long_description=(
          read('README.rst') +
          '.. contents::\n\n' +
          read('CHANGES.rst') +
          read('src', 'z3c', 'traverser', 'README.rst') +
          read('src', 'z3c', 'traverser', 'namespace.rst') +
          read('src', 'z3c', 'traverser', 'viewlet', 'README.rst') +
          read('src', 'z3c', 'traverser', 'viewlet', 'BROWSER.rst') +
          read('src', 'z3c', 'traverser', 'stackinfo', 'README.rst') +
          read('src', 'z3c', 'traverser', 'stackinfo', 'BROWSER.rst')
      ),
      keywords="zope3 traverser pluggable plugin viewlet",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: Implementation :: CPython',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope :: 3',
      ],
      url='https://github.com/zopefoundation/z3c.traverser',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['z3c'],
      python_requires='>=3.7',
      extras_require=dict(
          test=TESTS_REQUIRE,
      ),
      install_requires=(
          'setuptools',
          'zope.component',
          'zope.contentprovider',
          'zope.interface',
          'zope.publisher',
          'zope.traversing',
          'zope.viewlet',
          'zope.testrunner',
      ),
      include_package_data=True,
      zip_safe=False,
      )
