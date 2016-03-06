from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext

from other_core_functionalities.models import *

import logging

def homepage(request):
	logger = logging.getLogger(__name__)
	logger.error("FIRST RESPONSE")
	# return HttpResponse("DEAN ARMADA")
	template = "index.html"
	context_dict = {}
	return render(request, template, context_dict)

def error_page(request):
	return HttpResponse("WRONG PAGE")

def handler404(request):
	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response

def handler500(request):
	response = render_to_response('404.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response

@receiver(pre_save, sender=Name)
def sample_signal(sender, **kwargs):
	print ("SAMPLE SIGNAL")