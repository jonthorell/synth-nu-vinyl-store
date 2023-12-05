from products.models import product,genre,mediatype,testimonial
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order

def genres_context(request):
    genres = genre.objects.all()
    return {'genres': genres}
    
def mediatypes_context(request):
        mediatypes = mediatype.objects.all()
        return {'mediatypes': mediatypes}

def products_context(request):
        prods = product.objects.all()
        return {'products': prods}
        
def users_context(request):
        users = User.objects.prefetch_related("groups")
        return {'users': users}

def userprofiles_context(request):
        userprofiles = UserProfile.objects.all()
        return {'userprofiles': userprofiles}

def testimonials_context(request):
        testimonials = testimonial.objects.all()
        return {'testimonials': testimonials}

def orders_context(request):
        orders = Order.objects.all()
        return {'orders': orders}