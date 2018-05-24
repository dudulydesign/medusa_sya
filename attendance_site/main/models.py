# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class StaffRelatedEntry(models.Model):
  class Meta:
    unique_together = ("user", "staff_user")
  user = models.ForeignKey(User)
  staff_user = models.ForeignKey(User, related_name="staff_user")

