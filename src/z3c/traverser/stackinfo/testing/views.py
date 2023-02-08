##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
"""Testing Views
"""
from zope.traversing.browser.absoluteurl import absoluteURL

from z3c.traverser.stackinfo import interfaces


class StackInfoView:

    def __call__(self):
        url = absoluteURL(self, self.request)
        res = ['Stack Info from object at %s:' % url]
        for consumer in interfaces.ITraversalStackInfo(
                self.request):
            res.append('consumer %s:' % consumer.__name__)
            for arg in consumer.arguments:
                res.append('{} = {!r}'.format(arg, getattr(consumer, arg)))
        return '\n'.join(res)
