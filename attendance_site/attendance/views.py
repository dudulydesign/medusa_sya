from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.core.paginator import Paginator
from django.utils import timezone
from utils.paginations import generate_pagination
from .models import OvertimeEntry

from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from .forms import ApplyOvertimeForm

STATUS_WAIT = 0
STATUS_SUCCESS = 1
STATUS_CANCEL = 3

def status_to_text(status):
  if status == STATUS_WAIT:
    return u"審核中"

  if status == 1:
    return u"審核成功"

  if status == 2:
    return u"審核失敗"

  return "Nan"

'''
def leader_audit(request):

  if not request.user.is_authenticated():
    raise PermissionDenied
  return TemplateResponse(request, "attendance/leader_audit.html", {
    "pagination": pagination,
    })
'''

def overtime_list(request):

  if not request.user.is_authenticated():
    raise PermissionDenied

  page_number = 1
  try:
    page_number = int(request.GET["p"])
  except:
    pass
  
  qs = OvertimeEntry.objects
  qs = qs.filter(user_id=request.user.id).exclude(status=STATUS_CANCEL)
  qs = qs.order_by("-pub_date")

  pagination = generate_pagination(request, qs, 30)

  for obj in pagination.page.object_list:
    obj.minutes = round((obj.end_time - obj.start_time).total_seconds() / 60.0, 2)
    obj.status_name = status_to_text(obj.status)

  return TemplateResponse(request, "attendance/overtime_list.html", {
    "pagination": pagination, 
  })

def cancel_overtime(request):
  if request.user.is_authenticated():
    _id = int(request.GET["q"])

    try:
      entry = OvertimeEntry.objects.get(id=_id)
      if entry.user_id == request.user.id:
        entry.status = STATUS_CANCEL
        entry.save()
        return JsonResponse({
              "message": u"取消成功!",
              "code": 0,
          })
    except OvertimeEntry.DoesNotExist:
      pass

  #redirect_to = reverse_url("overtime_list")
  #return HttpResponseRedirect(redirect_to)
  return JsonResponse({
        "message": u"失敗",
        "code": 1,
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

      #now = datetime.now()  1999.1.1 +08:00
      now = timezone.now()   # 1999.1.1 +00:00

      delta = end_time - start_time
      print "delta", delta
      entry = OvertimeEntry(
          user = request.user,
          start_time = start_time,
          end_time = end_time,
          status=STATUS_WAIT,
          reason=reason,
          pub_date=now,
          )
      entry.save()
      redirect_to = reverse_url("overtime_list")
      return HttpResponseRedirect(redirect_to)
  else:
    form = ApplyOvertimeForm()

  return render(request, 'attendance/apply_overtime.html', {
    "form": form,
    })

