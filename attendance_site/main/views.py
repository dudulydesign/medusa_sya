from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url


def index(request):

  return TemplateResponse(request, "index.html", {
  })


def login_view(request):

  return TemplateResponse(request, "login.html", {
  })

def logout_view(request):

  return HttpResponseRedirect(reverse_url("index"))

