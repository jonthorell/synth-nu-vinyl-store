
from synth.decorators import check_user_is_staff
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


@check_user_is_staff
def staff(request):
    """ Display the staff only page. """
    
    template = 'staff/staff.html'
    context = {}
    
    

    return render(request, template, context)

@check_user_is_staff
def view_orders(request):
    """ Display the staff only page. """
    
    
    template = 'staff/view_orders.html'
    context = {
        # Order.objects.all()
        }
    
    

    return render(request, template, context)