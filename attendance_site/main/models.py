# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class LeaderRelatedEntry(models.Model):
  user = models.ForeignKey(User)
  leader_user = models.ForeignKey(User, related_name="leader_user")

