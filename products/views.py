from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from products.models import product, genre, artist
from django.contrib.auth.models import User

# from synth.utils import custom_mixin_kategorimenu

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = product.objects.all()
    query = None
    genres = None

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            products = products.filter(genre__name__in=genres)
            genres = genre.objects.filter(name__in=genres)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # need to alter this so can search for artist name
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_genres': genres,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    prod = get_object_or_404(product, pk=product_id)

    context = {
        'product': prod,
    }

    return render(request, 'products/product_details.html', context)