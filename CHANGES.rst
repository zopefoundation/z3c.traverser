=======
CHANGES
=======

2.0 (unreleased)
----------------

- Add support for Python 3.5, 3.6, 3.7, 3.8 and 3.9.

- Drop support for Python 2.6, 3.3 and 3.4.

- Drop support to run the tests using ``python setup.py test``.


1.0.0 (2015-11-09)
------------------

- Standardize namespace __init__.

- Claim support for Python 3.4.


1.0.0a2 (2013-03-03)
--------------------

- Added Trove classifiers to specify supported Python versions.


1.0.0a1 (2013-03-03)
--------------------

- Added support for Python 3.3.

- Replaced deprecated ``zope.interface.implements`` usage with equivalent
  ``zope.interface.implementer`` decorator.

- Dropped support for Python 2.4 and 2.5.

- Switched from ``zope.testbrowser`` to ``WebTest`` for browser testing, since
  testbrowser is not yet ported.

- Modernized API to use latest packages and component paths.

- Reduced test dependencies to the smallest set possible.


0.3.0 (2010-11-01)
------------------

- Updated test set up to run with ZTK 1.0.

- Using Python's ``doctest`` module instead of depreacted
  ``zope.testing.doctest[unit]``.


0.2.5 (2009-03-13)
------------------

- Adapt to the move of IDefaultViewName from zope.component to zope.publisher.

0.2.4 (2009-02-02)
------------------

- Make ``PluggableBrowserTraverser`` implement ``IBrowserPublisher``
  interface.
- Fix tests and deprecation warnings.
- Improve test coverage.
- Get rid of zope.app.zapi dependency by replacing its uses with direct
  calls.
- Change package's mailing list address to zope-dev at zope.org,
  because zope3-dev at zope.org is now retired.
- Change "cheeseshop" to "pypi" in the package's url.

0.2.3 (2008-07-14)
------------------

- Bugfix: In z3c.traverser.stackinfo the traversal stack got messed up
  when using the VirtualHost namespace with more than one thread.

0.2.2 (2008-03-06)
------------------

- Restructuring: Separated pluggable traverser functionality into two classes
  for better code reuse.


0.2.1 (2007-11-92)
------------------

- Bugfix: if viewlet and managers get nested a viewlet was not found if
  the depth reaches 3 because the context was set to the page and not
  to the context object.

- Bugfix: replaced call to ``_getContextName`` because it has been removed
  from ``absoluteURL``.


0.2.0 (2007-10-31)
------------------

- Update package meta-data.

- Resolve ``ZopeSecurityPolicy`` deprecation warning.


0.2.0b2 (2007-10-26)
--------------------

- Use only ``absolute_url`` adapters in unconsumed URL caclulations, to
  make it work for traversable viewlets or other special cases too.


0.2.0b1 (2007-09-21)
--------------------

- added a generic stack consumer handler which can be registered for
  BeforeTraverse events.


0.1.3 (2007-06-03)
------------------

- Added principal namespace, see ``namespace.rst``

- Fire ``BeforeUpdateEvent`` in viewlet view


0.1.1 (2007-03-22)
------------------

- First egg release


