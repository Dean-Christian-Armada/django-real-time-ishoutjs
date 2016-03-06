"""django_docs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

# from django.contrib.flatpages.sitemaps import FlatPageSitemap
# from django.contrib.sitemaps.views import sitemap
from django.conf.urls import include, url, handler400, handler403, handler404, handler500
# from django.contrib.flatpages import views as FlatpageViews
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.homepage, name="homepage"),
    # url(r'^error/$', views.error_page, name="error_page"),
    # url(r'^other-core-functionalities/', include('other_core_functionalities.urls'), name="other_core_functionalities"),
    # url(r'^sitemap\.xml$', sitemap,
    #     {'sitemaps': {'flatpages': FlatPageSitemap}},
    #     name='django.contrib.sitemaps.views.sitemap',
    # ),
    url(r'^real-time/', include('real_time.urls')),
]

# urlpatterns += [
#     url(r'^(?P<url>.*/)$', FlatpageViews.flatpage),
# ]