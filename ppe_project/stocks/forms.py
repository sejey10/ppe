from django.forms import ModelForm
from .models import Equipment, Used


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class UseEquipmentForm(ModelForm):
    class Meta:
        model = Used
        fields = '__all__'