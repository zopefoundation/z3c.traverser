from zope.traversing.browser import absoluteurl
from zope.traversing.browser.interfaces import IAbsoluteURL
import zope.component
import urllib

class ViewletAbsoluteURL(absoluteurl.AbsoluteURL):

    def __str__(self):
        context = self.context
        request = self.request

        # The application URL contains all the namespaces that are at the
        # beginning of the URL, such as skins, virtual host specifications and
        # so on.

        container = getattr(context, 'manager', None)
        if container is None:
            raise TypeError(absoluteurl._insufficientContext)

        url = str(zope.component.getMultiAdapter((container, request),
                                                 name='absolute_url'))

        name = self._getContextName(context)
        if name is None:
            raise TypeError(absoluteurl._insufficientContext)

        if name:
            url += '/' + urllib.quote(name.encode('utf-8'),
                                      absoluteurl._safe)

        return url

    def _getContextName(self, context):
        name = super(ViewletAbsoluteURL,
                     self)._getContextName(context)
        return u'++viewlet++' + name


    __call__ = __str__

class ViewletManagerAbsoluteURL(absoluteurl.AbsoluteURL):

    def _getContextName(self, context):
        name = super(ViewletManagerAbsoluteURL,
                     self)._getContextName(context)
        return u'++manager++' + name

class ViewletView(object):

    def __call__(self):
        self.context.update()
        return self.context.render()
    
        