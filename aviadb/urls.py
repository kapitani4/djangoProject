from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'^about', views.about, name='about'),
    re_path(r'^compartments/(?P<air_id>\d+)/', views.compartments, name='compartments'),
    re_path(r'^drawing', views.drawing, name='drawing'),
    path('', views.index, name='home')
]
