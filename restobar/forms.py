from django.forms import ModelForm
from .models import Reservations




class Reservationsform(ModelForm):
    class Meta:
        model = Reservations
        fields = '__all__'
    