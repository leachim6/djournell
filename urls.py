from django.conf.urls.defaults import *
from djournell.notes.models import Note,Courses

info_dict = {
        'queryset': Note.objects.all().order_by('-pub_date'),
        'paginate_by':10,
}

detail_dict = {
        'queryset': Note.objects.all(),
}

urlpatterns = patterns('',
        (r'^admin/', include('django.contrib.admin.urls')),
        (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
        (r'^note/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', detail_dict),
        (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/leachim6/src/python/djournell/public'}),
        (r'^course/(?P<course_slug>[-\w]+)/$', 'djournell.notes.views.notes_for_course'),
        (r'^courses?/$', 'djournell.notes.views.course_list'),
        (r'^edit/(?P<note_id>\d+)/$', 'djournell.notes.views.edit'),
        (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'notes/login.html'}),
        (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'notes/logout.html'}),
)
