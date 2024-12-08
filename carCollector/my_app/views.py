from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

cars = [
    Car('Ford', 'Mustang', 1964),
    Car('Chevy', 'Camaro', 1967),
    Car('Dodge', 'Charger', 1969),
]

def home(request):
    return HttpResponse('<h1>Hello Car guy!</h1>')

def about(request):
    return render(request, 'about.html')

def cars_index(request):

    return render(request, 'cars/index.html', {'cars': cars})

def cars_detail(request, car_id):
    car = cars[car_id]
    return render(request, 'cars/detail.html', {'car': car})