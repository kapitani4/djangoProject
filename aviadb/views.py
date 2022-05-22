from django.shortcuts import render
from .models import Drawing, Compartments, Aircraft

# Create your views here.
from django.http import HttpResponse


def index(request):
    air = Aircraft.objects.all()
    return render(request, 'aviadb/index.html', {'title' : 'Главная страница', 'air' : air})


def about(request):
    return render(request, 'aviadb/about.html')


def compartments(request, air_id):
    compartments = Compartments.objects.filter(model = air_id)
    return render(request, 'aviadb/compartments.html', {'title': 'Отсеки', 'compartments' : compartments})

def drawing(request, compartments_id):
    drawing = Drawing.objects.filter(detail = compartments_id)
    return render(request, 'aviadb/drawing.html', {'title': 'Чертежи', 'drawing' : drawing})

def plan(request, drawing_id):
    plan = Drawing.objects.filter(id = drawing_id)
    return render(request, 'aviadb/plan.html', {'title': 'Чертеж', 'plan': plan})