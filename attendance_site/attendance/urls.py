from django.conf.urls import url, include

import views

urlpatterns = [
    url(r'^overtime_list$', views.overtime_list, name="overtime_list"),
    url(r'^apply$', views.apply_overtime, name="apply_overtime"),
    url(r'^cancel_overtime$', views.cancel_overtime, name="overtime_cancel"),
    url(r'^leader_audit$', views.leader_audit, name="leader_audit"),
]
