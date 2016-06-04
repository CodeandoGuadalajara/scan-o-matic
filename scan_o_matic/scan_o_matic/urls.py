from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from scan_o_matic.views import hello, current_datetime, the_site
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scan_o_matic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url('', the_site),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
