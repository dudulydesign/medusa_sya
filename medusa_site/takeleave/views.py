# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.core.paginator import Paginator
from django.utils import timezone
from utils.paginations import generate_pagination
from .models import TakeleaveEntry
from main.models import StaffRelatedEntry
from django.core.exceptions import PermissionDenied
from .forms import ApplyTakeleaveForm, TakeleaveForm

"""
STATUS_WAIT = 0
STATUS_SUCCESS = 1
STATUS_REJECTED = 2
STATUS_CANCEL = 3

def status_to_text(status):
  if status == STATUS_WAIT:
    return u"審核中"

  if status == 1:
    return u"審核成功"

  if status == 2:
    return u"審核失敗"

  return "Nan"
"""

def takeleave_list(request):
  if not request.user.is_authenticated():
    raise PermissionDenied
  page_number = 1
  try:
    page_number = int(request.GET["p"])
  except:
    pass

  qs = TakeleaveEntry.objects
  qs = qs.filter(user=request.user.id).exclude(status=STATUS_CANCEL)
  qs = qs.order_by("-pub_date")

  pagination = generate_pagination(request, qs, 30)

  for obj in pagination.page.object_list:
    obj.minutes = round((obj.end_time - obj.start_time).total_seconds() / 60.0, 2)
    obj.status_name = status_to_text(obj.status)

  return TemplateResponse(request, "attendance/takeleave_list.html",{
    "pagination": pagination,
  })


def apply_takeleave(request):
  if not request.user.is_authenticated():
    raise PermissionDenied

  if request.method == "POST":
    form = ApplyTakeleaveForm(request.POST)
    if form.is_valid():
      print "->" * 100
      start_time = form.cleaned_data["start_time"]
      end_time = form.cleaned_data["end_time"]
      reason = form.cleaned_data["reason"]

      now = timezone.now()

      delta = end_time - start_time
      print "delta", delta
      entry = TakeleaveEntry(
          user = request.user,
          start_time = start_time,
          end_time = end_time,
          status = STATUS_WAIT,
          reason = reason,
          pub_date = now,
          )
      entry.save()
      
      redirect_to = reverse_url("takeleave_list")
      return HttpResponseRedirect(redirect_to)
  else:
    form = ApplyTakeleaveForm()

  return render(request, 'attendance/apply_takeleave.html', {
    "form": form,
    })
