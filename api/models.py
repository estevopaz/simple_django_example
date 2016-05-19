from __future__ import unicode_literals

from django.db import models

# Create your models here.

class New(models.Model):

    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    pub_date = models.DateField('date published')

    def __str__(self):
        return '{}, {}, {}'.format(self.title, self.body, self.pub_date)
