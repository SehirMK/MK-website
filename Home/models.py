from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class People(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264,unique=True)
    mails = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(People)
    date = models.DateField()

    def __str__(self):
        return str(self.date)