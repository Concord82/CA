from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from UserProfile.models import MyUser

# Create your models here.

class Contacts(models.Model):
    firstName = models.CharField(max_length=255,)
    lastName = models.CharField(max_length=255,)
    middleName = models.CharField(max_length=255,)
    depatament = models.CharField(max_length=255,)
    location = models.CharField(max_length=255,)
    city = models.CharField(max_length=255,)
    state = models.CharField(max_length=255,)
    country = models.CharField(max_length=2,)
    email = models.EmailField()

class CertList(models.Model):
    owner = models.ManyToManyField(MyUser)
    file_name = models.CharField(
        verbose_name=_('file_name'),
        max_length=255,
    )