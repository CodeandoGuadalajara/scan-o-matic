from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from scan_o_matic.views import current_datetime, the_site,nutricion,sobre_nosotros,que_es, ProcessImage
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scan_o_matic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', current_datetime),
    url('', the_site),
    url(r'^nutricion.html', nutricion),
    url(r'^que_es.html', que_es),
    url(r'^sobre_nosotros.html', sobre_nosotros),
    url(r'^upload/$', ProcessImage.as_view(), name='upload'),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
