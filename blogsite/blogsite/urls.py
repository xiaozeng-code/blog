from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/',include('ckeditor.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
