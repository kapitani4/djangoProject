from django.urls import re_path
from . import views

urlpatterns = [
    re_path('', views.index, name='home'),
    re_path('about', views.about, name='about'),
    re_path('compartments', views.compartments, name='compartments'),
    re_path('drawing', views.drawing, name='drawing')

]
