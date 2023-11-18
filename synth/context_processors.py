from products.models import product,genre,mediatype,product
from django.contrib.auth.models import User

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