from django.forms import ModelForm
from django import forms
from .models import Equipment, Used, Disposed


class DateInput(forms.DateInput):
    input_type = 'date'

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'date_of_receipt': DateInput(), # (A) here
        }

class UseEquipmentForm(ModelForm):
    class Meta:
        model = Used
        fields = ['equipment', 'date_being_used', 'qty_to_be_used']
        widgets = {
            'date_being_used': DateInput(), # (A) here
        }

