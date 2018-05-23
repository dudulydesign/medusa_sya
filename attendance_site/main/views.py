from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import LoginForm


def index(request):
  return TemplateResponse(request, "index.html", {
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
