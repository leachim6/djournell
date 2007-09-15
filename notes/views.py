from django.views.generic.list_detail import object_list
from cornell.notes.models import *

def notes_for_course(request, course_id):
    course = Course.objects.get(id=course_id)
    notes  = Course.note_set.all()
    return object_list(request, queryset=notes,template_name='Notes/notes_for_course.html',is_paginated=True,paginate_by=15)
