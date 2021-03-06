from django.conf.urls.defaults import *
from djournell.notes.models import Note,Courses
from django.contrib import admin
import os
admin.autodiscover()

info_dict = {
        'queryset': Note.objects.all().order_by('-pub_date'),
        'paginate_by':10,
}

detail_dict = {
        'queryset': Note.objects.all(),

}

urlpatterns = patterns('',
        (r'^admin/(.*)', admin.site.root),
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
        (r'^note/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', detail_dict),
        (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), "public") }),
        (r'^course/(?P<course_slug>[-\w]+)/$', 'djournell.notes.views.notes_for_course'),
        (r'^courses?/$', 'djournell.notes.views.course_list'),
        (r'^edit/(?P<note_id>\d+)/$', 'djournell.notes.views.edit'),
        (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'notes/login.html'}),
        (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'notes/logout.html'}),
)
