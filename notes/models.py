from django.db import models

class Note(models.Model):
    title = models.CharField()
    course = models.ManyToManyField(Courses)
    keycol = models.TextField()
    bodycol = models.TextField()
    pub_date = models.DateTimeField()
    comments_enabled = models.BooleanField

class Courses(models.Model):
    name = models.CharField()
