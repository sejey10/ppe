from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


from .forms import EquipmentForm, UseEquipmentForm
from .models import Equipment, Used


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
        form.save()
        return redirect(home)
    print('failed to submit form')
    context = {
        'form': form,
    }
    return render(request, template_name, context=context)



def use_equipment(request):
    template_name = 'equipment/use_equipment.html'
    form = UseEquipmentForm()

    if request.method == 'POST':
        form = UseEquipmentForm(request.POST)
        form.save()
        return redirect(home)
    print('failed to submit form')
    context = {
        'form': form,
    }


    return render(request, template_name, context=context)

