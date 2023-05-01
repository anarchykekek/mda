from .models import *
from django.forms import *

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name", "age", "area", "address"]

        widgets = {
            "name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Имя"
            } ),
            "age": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Возраст"
            }),
            "area": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Район проживания"
            }),
            "address": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Адрес"
            })

        }
