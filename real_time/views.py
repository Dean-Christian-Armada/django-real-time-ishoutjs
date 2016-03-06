from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from drealtime import iShoutClient
ishout_client = iShoutClient()

from . models import *

# Create your views here.
@login_required
def index(request):
	# return HttpResponse("dasdas")
	users = User.objects.exclude(id=request.user.id)
	sections = Section.objects.filter()
	# ishout_client.emit(
	# 	1,
	# 	'notifications',
	# 	data={'msg':'You a new section!'}
	# )
	template = "real_time/index.html"
	# context_dict = {'sections': sections, 'users':users}
	context_dict = RequestContext(request,{'sections': sections, 'users':users})
	# return render(request, template, context_dict)
	return render_to_response(template, context_dict)

@login_required
def test(request):
	print (request.user.id)
	users = User.objects.exclude(id=request.user.id)
	template = "real_time/test.html"
	context_dict = {'users':users}
	# context_dict = RequestContext
	# return render(request, template, context_dict)
	return render_to_response(template, context_dict)

@login_required
def alert(request):
	# return HttpResponse("dean")
	r = request.GET.get
	print (int(r('user')))
	print (ishout_client)
	ishout_client.emit(
		int(r('user')),
		'alertchannel',
		data={'msg':'You a new section!'}
	)
	return HttpResponseRedirect(reverse('test'))