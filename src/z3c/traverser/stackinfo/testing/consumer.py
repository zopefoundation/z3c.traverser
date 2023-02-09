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
"""Testing Consumer
"""
from zope import component
from zope import interface
from zope.location.interfaces import ISite
from zope.publisher.interfaces.browser import IBrowserRequest

from z3c.traverser.stackinfo import interfaces
from z3c.traverser.stackinfo.consumer import BaseConsumer


@interface.implementer(interfaces.ITraversalStackConsumer)
@component.adapter(ISite, IBrowserRequest)
class KeyValueConsumer(BaseConsumer):
    arguments = ('key', 'value')
