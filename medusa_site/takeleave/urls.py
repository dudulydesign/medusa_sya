from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^takeleave_list$', views.takeleave_list, name="takeleave_list"),
    url(r'^apply_takeleave$', views.apply_takeleave, name="apply_takeleave"),
]
