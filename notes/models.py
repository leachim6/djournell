from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.name

class Note(models.Model):
    title = models.CharField(max_length=40)
    course = models.ManyToManyField(Courses)
    keycol = models.TextField()
    bodycol = models.TextField()
    pub_date = models.DateTimeField()
    comments_enabled = models.BooleanField()

    def __unicode__(self):
        return self.title
