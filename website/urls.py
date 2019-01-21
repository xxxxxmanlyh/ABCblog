"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry
from blog import views as blog_views
from django.views.static import serve

info_dict = {
    'queryset':Entry.objects.all(),
    'date_field': 'modified_time'
}

urlpatterns = [
    url(r'^$',blog_views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^captcha', include('captcha.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT }, name='static'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT }, name='media'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^sitemap\.xml$',sitemap,{'sitemaps':{'blog': GenericSitemap(info_dict,priority=0.6)}},name='django.contrib.sitemaps.views.sitemap'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
