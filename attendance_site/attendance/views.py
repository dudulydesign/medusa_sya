from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url

def index(request):

  return TemplateResponse(request, "attendance/index.html", {
  })
