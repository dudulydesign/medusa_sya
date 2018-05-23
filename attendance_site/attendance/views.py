from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.core.paginator import Paginator
from utils.paginations import generate_pagination
from .models import OvertimeEntry


def status_to_text(status):
  if status == 0:
    return u"審核中"

  if status == 1:
    return u"審核成功"

  if status == 2:
    return u"審核失敗"

  return "Nan"

def index(request):

  page_number = 1
  try:
    page_number = int(request.GET["p"])
  except:
    pass
  
  qs = OvertimeEntry.objects

  qs = qs.order_by("-pub_date")

  pagination = generate_pagination(request, qs, 30)

  for obj in pagination.page.object_list:
    obj.minutes = round((obj.end_time - obj.start_time).total_seconds() / 60.0, 2)
    obj.status_name = status_to_text(obj.status)

  return TemplateResponse(request, "attendance/index.html", {
    "pagination": pagination, 
  })
