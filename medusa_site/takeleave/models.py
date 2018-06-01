# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

  
class TakeleaveEntry(models.Model):
  user = models.ForeignKey(User)
  status = models.IntegerField()
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  reason = models.TextField()
  pub_date = models.DateTimeField()
  date_created = models.DateTimeField(auto_now_add=True)

class TakeleaveApplyEntry(models.Model):
  user = models.ForeignKey(User)
  takeleave = models.ForeignKey(TakeleaveEntry)
  time = models.DateTimeField()
  date_created = models.DateTimeField(auto_now_add=True)

