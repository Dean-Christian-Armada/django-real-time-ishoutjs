from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="real_time_index"),
	url(r'alert/$', views.alert, name="real_time_alert"),
	url(r'test/$', views.test, name="test"),
	url(r'login/$', 'django.contrib.auth.views.login'),
]