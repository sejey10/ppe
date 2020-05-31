from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .forms import EquipmentForm, UseEquipmentForm
from .models import Equipment, Used, Disposed


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
@login_required
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

@login_required
def detailed_equipment(request, id):
    template_name = 'equipment/detailed_equipment.html'
    equipment = Equipment.objects.get(id=id)
    total_used_equipment = Used.objects.all().filter(equipment=id).filter(is_used=True)
    disposed = Disposed.objects.all().filter(equipment=id)
    not_used_equipment = Used.objects.all().filter(equipment=id).filter(is_used=False)

    total_disposed = 0
    for dis in disposed:
        total_disposed += dis.qty_to_be_disposed

    total_used = 0
    for use in total_used_equipment:
        total_used += use.qty_to_be_used

    total_available = equipment.qty_per_package - total_used - total_disposed
    


    context = {
        'equipment': equipment,
        'total_used': total_used,
        'total_available': total_available,
        'total_used_equipment': total_used_equipment,
        'total_disposed': total_disposed,
        'disposed': disposed,
        'not_used_equipment': not_used_equipment,
    }

    return render(request, template_name, context=context)



@login_required
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

@login_required
def dispose_equipment(request, id):
    to_be_disposed = Used.objects.get(id=id)

    disposed, created =  Disposed.objects.get_or_create(
                        equipment=to_be_disposed.equipment,
                        qty_to_be_disposed=to_be_disposed.qty_to_be_used
                        )  
    to_be_disposed.is_used = False
    to_be_disposed.save()
    
    


    return redirect(home)