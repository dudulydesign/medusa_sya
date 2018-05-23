from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^overtime_list$', views.overtime_list, name="overtime_list"),
]
