from django.forms import ModelForm
from my_cars.models import Car

class CarForm(ModelForm):
    class Meta:
        model = Car