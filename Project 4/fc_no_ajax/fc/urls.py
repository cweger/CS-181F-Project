'''
This file was authored by Michael and Chet.

It maps urls to view functions using regular expressions.
'''

from django.conf.urls.defaults import *
from models import cardTable
from models import userSetTable

notes = cardTable.objects.all()

urlpatterns = patterns(
    '',
	#Chet's:
	(r'^set/(?P<setID>[-\w]+)/$','fc.views.list_card'),

	(r'^set/(?P<setID>[-\w]+)/card/(?P<cardID>[-\w]+)/delete_card/$', 'fc.views.delete_card'),

	(r'^set/(?P<setID>[-\w]+)/card/(?P<cardID>[-\w]+)/$','fc.views.show_card'),
	(r'^create/(?P<setID>[-\w]+)/$','fc.views.create_card'),
	(r'^set/(?P<setID>[-\w]+)/card/(?P<cardID>[-\w]+)/update/$','fc.views.update_card'),

	#Michael's
	(r'^$','fc.views.list_materials'),
	(r'^user/$','fc.views.list_materials'),

	(r'^user/set/(?P<setID>[-\w]+)/delete_set/$', 'fc.views.delete_set'),
	
#	(r'^user/group/(?P<groupID>[-\w]+)/leave_group/$', 'fc.views.leave_group'),

	(r'^user/log_out/','fc.views.log_out'),
	(r'^create_set/$','fc.views.create_set'),
)
