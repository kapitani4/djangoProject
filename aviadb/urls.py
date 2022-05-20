from django.urls import re_path, path
from . import views

urlpatterns = [
    #re_path('', views.index, name='home'),
    path('',views.index, name='home'),
    re_path(r'^about', views.about, name='about'),
    re_path(r'^compartments', views.compartments, name='compartments'),
    re_path(r'^drawing', views.drawing, name='drawing')

]
