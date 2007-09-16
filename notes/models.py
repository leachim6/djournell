from django.db import models

class Courses(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name

    class Admin:
        pass

    class Meta:
        verbose_name_plural = 'Courses'

class Note(models.Model):
    title = models.CharField(max_length=40)
    course = models.ManyToManyField(Courses)
    keycol = models.TextField()
    bodycol = models.TextField()
    sumcol = models.TextField()
    pub_date = models.DateTimeField()
    comments_enabled = models.BooleanField()

    def __unicode__(self):
        return self.title

    class Admin:
        pass
