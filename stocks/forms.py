from django.forms import ModelForm
from django import forms
from .models import Equipment, Used, DisposedEquipment


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

    def __init__(self, *args, **kwargs):
        super(UseEquipmentForm, self).__init__(*args, **kwargs)
        self.fields['equipment'].queryset = Equipment.objects.all().filter(is_deleted=False)

    class Meta:
        model = Used

        fields = ['equipment', 'date_being_used', 'qty_to_be_used']
        widgets = {
            'date_being_used': DateInput(), # (A) here
        }

