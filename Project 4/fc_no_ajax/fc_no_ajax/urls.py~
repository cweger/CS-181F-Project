from django.conf.urls.defaults import *
from django.conf import settings
urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    (r'^', include('fc.urls')), #<-- modified (correctly) include: interesting function (I think it says: include( url patterns from notes folder )
)
