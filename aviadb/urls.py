from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('compartments', views.compartments, name='compartments'),
    path('drawing', views.drawing, name='drawing')

]
