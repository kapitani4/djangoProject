from django.shortcuts import render
from .models import Drawing, Compartments, Aircraft

# Create your views here.
from django.http import HttpResponse


def index(request):
    air = Aircraft.objects.all()
    return render(request, 'aviadb/index.html', {'title' : 'Главная страница', 'air' : air})


def about(request):
    return render(request, 'aviadb/about.html')


def compartments(request):
    compartments = Compartments.objects.all()
    return render(request, 'aviadb/compartments.html', {'title': 'Отсеки', 'compartments' : compartments})

def drawing(request):
    drawing = Drawing.objects.all()
    return render(request, 'aviadb/drawing.html', {'title': 'Чертежи', 'drawing' : drawing})