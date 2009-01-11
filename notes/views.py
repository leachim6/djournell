from django.views.generic.list_detail import object_list
from djournell.notes.models import *
from django import forms as forms
from django.forms import ModelForm
from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponseRedirect

def notes_for_course(request, course_slug):
    course = Courses.objects.get(slug=course_slug)
    notes  = course.note_set.all()
    return object_list(request, queryset=notes,template_name='Notes/notes_for_course.html',paginate_by=15)

def course_list(request):
    course_list = Courses.objects.all()
    return object_list(request, queryset=course_list,template_name='Notes/course_list.html',paginate_by=15)

def template(req, *args, **kwargs):
	kwargs['context_instance'] = RequestContext(req)
	return render_to_response(*args, **kwargs)

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note

def edit(request, note_id):
  if note_id is not None:
    note = get_object_or_404(Note, id=note_id)
  else:
    note = None

  form = NoteForm(data=request.POST or None, instance=note)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect("/note/"+note_id)

  return  render_to_response('notes/edit_note.html', {'form': form, 'note_id': note_id, 'request': request})
