

from synth.decorators import check_user_is_staff
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages


from products.models import testimonial
from core.models import contact_message

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

@check_user_is_staff
def handle_contact_messages(request):
    '''Class used for handling contact messages '''
    
    # it is only handling handled/not handled. It could certainly be extended with stuff like "Waiting for user", "Out of scope"
    # and other things for a bigger site

    contact_messages = contact_message.objects.filter(complete=0).all()

    context = {
        'contact_messages': contact_messages,
    }

    return render(request, 'staff/handle_contact.html', context)

@check_user_is_staff
def handled(request, handled_id):
    """ Update db with new approved status """
    contact_message.objects.filter(pk=handled_id).update(complete=1)
    messages.success(request, 'Message handled!')
    return redirect('/')