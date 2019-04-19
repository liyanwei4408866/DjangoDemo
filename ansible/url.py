from django.conf.urls import url
from django.urls import path,re_path

from . import views
urlpatterns = [
    path('',views.index),
    re_path(r'^(\d+)/(\d+)$',views.detail),
    path('grade/',views.grade),
    path('student/',views.student),
    re_path(r'^grade/(\d+)$',views.studentByGradeId),
]