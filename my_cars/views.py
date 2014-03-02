# Create your views here.
import csv
from django.shortcuts import render, redirect
from my_cars.forms import CarForm
from my_cars.models import Car

def home(request):
    return render(request, 'home.html')

def get_car_data(request):
    with open("my_cars/static/cars.csv", "rU") as f:
        reader = csv.reader(f)
        for row in reader:
            Car.objects.create(year=row[0], make=row[1], model=row[2], horsepower=row[3], transmission=row[4])
            # return redirect("/car")

def cars(request):
    cars = Car.objects.all()
    data = {'cars':cars}
    return render(request, "car/car.html", data)

def new_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/car")

    else:
        form = CarForm()
    data = {'form':form}
    return render(request, "car/new_car.html", data)


def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            if form.save():
                return redirect("/car{}".format(car_id))

    else:
        form = CarForm(instance=car)
    data = {'form':form}
    return render(request, "car/edit_car.html", data)


def view_car(request, car_id):
    car = Car.objects.get(id=car_id)
    data = {'car':car}
    return render(request, "car/view_car.html", data)


def delete_car(request, car_id):
    car = Car.objects.all(id=car_id)
    car.delete()
    return render(request, "car/car.html")