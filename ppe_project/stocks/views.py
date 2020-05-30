from django.shortcuts import render, redirect


from .forms import EquipmentForm
from .models import Equipment


# Home Page
def home(request):
	template_name = 'home/index.html'
	return render(request, template_name, context=None)


# Show All Equipment Page
def show_all_equipment(request):
    template_name = 'equipment/show_all_equipment.html'
    all_equipment = Equipment.objects.all()
    context = {
        'all_equipment': all_equipment
    }
    return render(request, template_name, context=context)



# Add Equipment Page
def add_equipment(request):
    template_name = 'equipment/add_equipment.html'
    form = EquipmentForm()
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        return redirect(home)
    context = {
        'form': form,
    }
    return render(request, template_name, context=context)