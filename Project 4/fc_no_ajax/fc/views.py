from django.core.context_processors import csrf
from models import cardTable
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseServerError
from django.shortcuts import render

def list_card(request):
	cardList = cardTable.objects.order_by('cardID')
	return render(request, 'fc/test.html', {'card_list': cardList,})
