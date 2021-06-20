# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200, unique=True)
    username=models.CharField(max_length=200, unique=True)
    password=models.CharField(max_length=200)
    status=models.IntegerField(default=0)
    role=models.CharField(max_length=200)
    mob=models.CharField(max_length=200,default="9847563210")

class files(models.Model):
    name=models.CharField(max_length=200)
    path=models.CharField(max_length=200, unique=True)
    desc=models.CharField(max_length=200, unique=True)
    username=models.CharField(max_length=200)

