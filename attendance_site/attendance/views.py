from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.core.paginator import Paginator
from utils.paginations import generate_pagination
from .models import OvertimeEntry

from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .forms import ApplyOvertimeForm


def status_to_text(status):
  if status == 0:
    return u"審核中"

  if status == 1:
    return u"審核成功"

  if status == 2:
    return u"審核失敗"

  return "Nan"

def overtime_list(request):

  if not request.user.is_authenticated():
    raise PermissionDenied

  page_number = 1
  try:
    page_number = int(request.GET["p"])
  except:
    pass
  
  qs = OvertimeEntry.objects

  #qs = qs.filter(?)

  qs = qs.order_by("-pub_date")

  pagination = generate_pagination(request, qs, 30)

  for obj in pagination.page.object_list:
    obj.minutes = round((obj.end_time - obj.start_time).total_seconds() / 60.0, 2)
    obj.status_name = status_to_text(obj.status)

  return TemplateResponse(request, "attendance/overtime_list.html", {
    "pagination": pagination, 
  })


def apply_overtime(request):
  if not request.user.is_authenticated():
    raise PermissionDenied

  if request.method == "POST":
    form = ApplyOvertimeForm(request.POST)
    if form.is_valid():
      print "->" * 100
      start_time = form.cleaned_data["start_time"]
      end_time = form.cleaned_data["end_time"]
      reason = form.cleaned_data["reason"]

      delta = end_time - start_time
      print "delta", delta
      entry = OvertimeEntry(
          user = request.user,
          start_time = start_time,
          end_time = end_time,
          reason = reason
          )
      entry.save()
      redirect_to = reverse_url("index")
      return HttpResponseRedirect(redirect_to)
  else:
    form = ApplyOvertimeForm()
  return render(request, 'attendance/apply_overtime.html', {
    "form": form,
    })

