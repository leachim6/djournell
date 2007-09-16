from django.views.generic.list_detail import object_list
from cornell.notes.models import *
from django import newforms as forms
from django.shortcuts import *
from django.template import RequestContext

def notes_for_course(request, course_slug):
    course = Courses.objects.get(slug=course_slug)
    notes  = course.note_set.all()
    return object_list(request, queryset=notes,template_name='Notes/notes_for_course.html',paginate_by=15)

def course_list(request):
    course_list = Courses.objects.all()
    return object_list(request, queryset=course_list,template_name='Notes/course_list.html',paginate_by=15)

def edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    f = forms.form_for_instance(note)()
    form_dict = {
            'form': f,
            'note_id': note_id,
            }
    return render_to_response('notes/edit_note.html', form_dict, context_instance=RequestContext(request))
