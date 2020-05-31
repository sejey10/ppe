from django.forms import ModelForm
from .models import Equipment, Used, Disposed


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class UseEquipmentForm(ModelForm):
    class Meta:
        model = Used
        fields = ['equipment', 'date_being_used', 'qty_to_be_used']


