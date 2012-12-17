from django.conf.urls.defaults import *
from models import cardTable

notes = cardTable.objects.all()

urlpatterns = patterns(
    '',
	(r'^$','fc.views.list_card'),
	(r'^set/$','fc.views.list_card'),
)
