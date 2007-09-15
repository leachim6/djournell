from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^cornell/', include('cornell.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
