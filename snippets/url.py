from django.conf.urls import url
from django.urls import path,re_path

from . import views
urlpatterns = [
    re_path(r'^$', views.snippet_list),
    re_path(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),

]