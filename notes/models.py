from django.db import models
from django.contrib import admin


class Courses(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Courses'

class Note(models.Model):
    title = models.CharField(max_length=40)
    course = models.ManyToManyField(Courses)
    keycol = models.TextField(blank=True)
    bodycol = models.TextField(blank=True)
    sumcol = models.TextField(blank=True)
    pub_date = models.DateTimeField(blank=False)
    comments_enabled = models.BooleanField()
    upload = models.FileField(upload_to='public/%Y/%m/%d', blank=True)

    def __unicode__(self):
        return self.title

    class Admin:
        fields = (
                ('Details', {'fields': ('title','course','pub_date',)}),
                ('Information', {'fields': ('keycol','bodycol','sumcol',)}),
                ('Experimental', {'fields': ('comments_enabled','upload',), 'classes': 'collapse'}),
                )

admin.site.register(Courses)
admin.site.register(Note)
