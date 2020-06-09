from django.shortcuts import render
import json
# stocks
from stocks.models import Equipment, Used, Disposed

from django.http import HttpResponse
from django.db.models import Sum


def home(request):
    template_name = 'analytics/index.html'

    # total masks
    total_masks = Equipment.objects.filter(item_name='MSK')
    total_used_masks_q = Used.objects.all().filter(is_used=True).filter(equipment__item_name__contains='MSK')
    total_unused_masks_q = Used.objects.all().filter(is_used=False).filter(equipment__item_name__contains='MSK')
    total_disposed_masks_q = Disposed.objects.all().filter(equipment__item_name__contains='MSK')

    total_masks_qty = 0
    for mask in total_masks:
        total_masks_qty += mask.qty_per_package

    total_used_masks = 0
    for use in total_used_masks_q:
        total_used_masks += use.qty_to_be_used

    total_disposed_masks = 0
    for dis in total_disposed_masks_q:
        total_disposed_masks += dis.qty_to_be_disposed

    total_available_masks = total_masks_qty - total_used_masks - total_disposed_masks




    # total gogss
    total_gogs = Equipment.objects.filter(item_name='GOG')
    total_used_gogs_q = Used.objects.all().filter(is_used=True).filter(equipment__item_name__contains='GOG')
    total_unused_gogs_q = Used.objects.all().filter(is_used=False).filter(equipment__item_name__contains='GOG')
    total_disposed_gogs_q = Disposed.objects.all().filter(equipment__item_name__contains='GOG')

    total_gogs_qty = 0
    for mask in total_gogs:
        total_gogs_qty += mask.qty_per_package

    total_used_gogs = 0
    for use in total_used_gogs_q:
        total_used_gogs += use.qty_to_be_used

    total_disposed_gogs = 0
    for dis in total_disposed_gogs_q:
        total_disposed_gogs += dis.qty_to_be_disposed

    total_available_gogs = total_gogs_qty - total_used_gogs - total_disposed_gogs

   # total gowns
    total_gown = Equipment.objects.filter(item_name='GWN')
    total_used_gown_q = Used.objects.all().filter(is_used=True).filter(equipment__item_name__contains='GWN')
    total_unused_gown_q = Used.objects.all().filter(is_used=False).filter(equipment__item_name__contains='GWN')
    total_disposed_gown_q = Disposed.objects.all().filter(equipment__item_name__contains='GWN')

    total_gown_qty = 0
    for mask in total_gown:
        total_gown_qty += mask.qty_per_package

    total_used_gown = 0
    for use in total_used_gown_q:
        total_used_gown += use.qty_to_be_used

    total_disposed_gown = 0
    for dis in total_disposed_gown_q:
        total_disposed_gown += dis.qty_to_be_disposed

    total_available_gown = total_gown_qty - total_used_gown - total_disposed_gown



    total_caps = Equipment.objects.filter(item_name='CPS')
    total_used_caps_q = Used.objects.all().filter(is_used=True).filter(equipment__item_name__contains='CPS')
    total_unused_caps_q = Used.objects.all().filter(is_used=False).filter(equipment__item_name__contains='CPS')
    total_disposed_caps_q = Disposed.objects.all().filter(equipment__item_name__contains='CPS')

    total_caps_qty = 0
    for mask in total_caps:
        total_caps_qty += mask.qty_per_package

    total_used_caps = 0
    for use in total_used_caps_q:
        total_used_caps += use.qty_to_be_used

    total_disposed_caps = 0
    for dis in total_disposed_caps_q:
        total_disposed_caps += dis.qty_to_be_disposed

    total_available_caps = total_caps_qty - total_used_caps - total_disposed_caps


    total_available = total_available_caps + total_available_gown + total_available_gogs + total_available_masks


    # pie chart test
    dates = []
    qty = []
    # used equipment
    used_q = Used.objects.filter().values('date_being_used').order_by('date_being_used').annotate(sum=Sum('qty_to_be_used'))
    for use in used_q:
        date = use['date_being_used']
        qt = use['sum']
        dates.append(str(date))
        qty.append(qt)
   
    print(dates)
    print(qty)
    context = {
        # gogs
        'total_gogs_qty':total_gogs_qty,
        'total_used_gogs': total_used_gogs,
        'total_disposed_gogs': total_disposed_gogs,
        'total_available_gogs': total_available_gogs,

        # caps
        'total_caps_qty':total_caps_qty,
        'total_used_caps': total_used_caps,
        'total_disposed_caps': total_disposed_caps,
        'total_available_caps': total_available_caps,

        # masks

        'total_masks_qty':total_masks_qty,
        'total_used_masks': total_used_masks,
        'total_disposed_masks': total_disposed_masks,
        'total_available_masks': total_available_masks,

        # gowns
        'total_gown_qty':total_gown_qty,
        'total_used_gown': total_used_gown,
        'total_disposed_gown': total_disposed_gown,
        'total_available_gown': total_available_gown,

        'total_available': total_available,

        'used': used_q,
        'dates': dates,
        'qty': qty,

        
    
    }




    return render(request, template_name, context=context)

