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


def detailed_equipment(request, id):
    template_name = 'equipment/detailed_equipment.html'
    equipment = Equipment.objects.get(id=id)
    total_used_equipment = Used.objects.all().filter(equipment=id)
    total_used = 0
    for use in total_used_equipment:
        total_used += use.qty_to_be_used

    total_available = equipment.qty_per_package - total_used
    
    # detailed = list(total_used_equipment)

    # detailed_qty = []
    # detailed_date = []
    # for detailed_use in detailed:
    #     date = detailed_use.qty_to_be_used
    #     quantity = detailed_use.date_being_used
        
    #     detailed_date.append(date)
    #     detailed_qty.append(quantity)



    context = {
        'equipment': equipment,
        'total_used': total_used,
        'total_available': total_available,
        'total_used_equipment': total_used_equipment,
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

