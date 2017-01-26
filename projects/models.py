from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.

class ProjectPost(models.Model):
    title = models.CharField(max_length=250)
    bodytext = models.TextField()

    post_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = ('post')
        verbose_name_plural = ('posts')
        ordering = ['-modified_date']

    def __str__(self):
        return self.title
