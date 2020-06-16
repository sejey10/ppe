from django.forms import ModelForm
from django import forms
from .models import Equipment, Used, DisposedEquipment


class DateInput(forms.DateInput):
    input_type = 'date'

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['package_number', 'item_name',
                    'qty_per_package', 'condition_upon_received',
                    'supplier', 'received_by', 'checked_by',
                    'date_of_receipt']
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

