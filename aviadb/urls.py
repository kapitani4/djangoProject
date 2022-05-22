from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^about', views.about, name='about'),
    re_path(r'^compartments/(?P<air_id>[0-9])/', views.compartments, name='compartments'),
    re_path(r'^drawing/(?P<compartments_id>[0-9])/', views.drawing, name='drawing'),
    re_path(r'^plan/(?P<drawing_id>[0-9])/', views.plan, name='plan'),
    path('', views.index, name='home')
]
