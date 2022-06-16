from django.urls import re_path, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^about', views.about, name='about'),
    re_path(r'^compartments/(?P<air_id>[0-9]{1,3})/', views.compartments, name='compartments'),
    re_path(r'^drawing/(?P<compartments_id>[0-9]{1,3})/', views.drawing, name='drawing'),
    re_path(r'^plan/(?P<drawing_id>[0-9]{1,3})/', views.plan, name='plan'),
    re_path(r'^plan/(?P<drawing_id>[0-9]{1,3})/files/(?P<filename>)', views.files, name='plan'),
    path('', views.index, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
