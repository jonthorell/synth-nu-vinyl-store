from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
import urllib.parse
from products.models import product, genre, artist, mediatype
from django.contrib.auth.models import User

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = product.objects.all()
    query = None
    genres = None
    types= None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'genre':
                sortkey = 'genre__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            products = products.filter(genre__name__in=genres)
            genres = genre.objects.filter(name__in=genres)
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            products = products.filter(media_format__name__in=types)
            types = mediatype.objects.filter(name__in=types)
        if 'q' in request.GET:
            query = request.GET['q']
            query = urllib.parse.unquote(query)
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # need to alter this so can search for artist name
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(artist__name__icontains=query)
            products = products.filter(queries)
            
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_genres': genres,
        'current_sorting': current_sorting,
        'current_mediatypes': types,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    prod = get_object_or_404(product, pk=product_id)

    context = {
        'product': prod,
    }

    return render(request, 'products/product_details.html', context)