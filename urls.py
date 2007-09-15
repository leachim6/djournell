from django.conf.urls.defaults import *
from cornell.notes.models import Note,Courses

info_dict = {
        'queryset': Note.objects.all().order_by('-pub_date'),
        'paginate_by':10,
}

urlpatterns = patterns('',
        (r'^admin/', include('django.contrib.admin.urls')),
        (r'^$', 'django.views.generic.list_detail.object_list', info_dict) 
)
