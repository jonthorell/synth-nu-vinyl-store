

from synth.decorators import check_user_is_staff
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages


from products.models import testimonial

@check_user_is_staff
def staff(request):
    """ Display the staff only page. """
    
    template = 'staff/staff.html'
    context = {}
    
    

    return render(request, template, context)

@check_user_is_staff
def view_orders(request):
    """ Display the view all orders page. """
    
    
    template = 'staff/view_orders.html'
    context = {}
    
    

    return render(request, template, context)

@check_user_is_staff    
def approve_review(request):
    '''Class used for approving reviews '''

    testimonials = testimonial.objects.filter(approved=False).all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'staff/approve_review.html', context)

@check_user_is_staff
def update_review(request, review_id):
    """ Update db with new approved status """
    testimonial.objects.filter(pk=review_id).update(approved=True)
    messages.success(request, 'Review approved!')
    return redirect('/products/?genre=classic,electronica,ebm,experimental,industry,spop,euro')