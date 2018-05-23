# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse as reverse_url
from django.contrib.auth import logout as auth_logout, login as auth_login
from main.forms import LoginForm


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
