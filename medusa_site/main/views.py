from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import LoginForm

from attendance.views import leader_audit_list
from main.models import StaffRelatedEntry
from attendance.models import OvertimeEntry

STATUS_WAIT = 0


def index(request):
  if not request.user.is_authenticated():
    return HttpResponseRedirect(reverse_url("login"))

  #overtime_count = 1
  overtime_count = list(StaffRelatedEntry.objects.filter(user_id=request.user.id).all())
  arr = [overtime_count]
  arr_appear = dict((a, overtime_count.count(a)) for a in overtime_count);
  print arr_appear;
  
  '''
  qs = OvertimeEntry.objects
  qs = qs.filter(status=STATUS_WAIT)
  qs = qs.filter(user_id__in=arr_appear)
  qs = qs.order_by("-pub_date")
  '''


  return TemplateResponse(request, "index.html", {
    "overtime_count":overtime_count
  })

def login_view(request):
  print "=>" * 100
  print "login_view"
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      print "is_valid!!!"
      user = form.user
      auth_login(request, user)
      url2 = reverse_url("index")
      return HttpResponseRedirect(url2)
  else:
    form = LoginForm()
  return TemplateResponse(request, "login.html", {
    "login_form": form,
    })

def logout_view(request):
  auth_logout(request)
  url2 = reverse_url("index")
  return HttpResponseRedirect(url2)
