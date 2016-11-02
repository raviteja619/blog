from __future__ import unicode_literals
import os
import datetime
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
def get_file_path(instance, filename):
    if instance:
        return os.path.join("static", 'uploads', str(instance.slug), filename)


class Blog(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.FileField(upload_to=get_file_path, null=True, blank=True)
    creator = models.ForeignKey(User)
    body = RichTextField()
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.title
