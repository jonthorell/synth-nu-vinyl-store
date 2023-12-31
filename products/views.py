
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
import urllib.parse
from products.models import product, genre, artist, mediatype, testimonial
from .forms import ProductForm,GenreForm, CommentForm
from django.contrib.auth.models import User
from synth.decorators import check_user_is_staff, check_user_is_member

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
            
            
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(artist__friendly_name__icontains=query)
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

@check_user_is_staff
def add_product(request):
    """ Add a product to the store """
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[prod.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@check_user_is_staff
def edit_product(request, product_id):
    """ Edit a product in the store """
    prod = get_object_or_404(product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[prod.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=prod)
        messages.info(request, f'You are editing {prod.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': prod,
    }

    return render(request, template, context)

@check_user_is_staff
def add_genre(request):
    """ Add a new genre to the store """
    
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added genre!')
            return redirect(reverse('/staff'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = GenreForm()

    template = 'products/add_genre.html'
    context = {
        'form': form,
    }
    return render(request, template, context)

@check_user_is_staff
def delete_product(request, product_id):
    """ Delete a product from the store """
    prod = get_object_or_404(product, pk=product_id)
    prod.delete()
    messages.success(request, 'Product deleted!')
    return redirect('/products/?genre=classic,electronica,ebm,experimental,industry,spop,euro')

@check_user_is_member
def review_product(request, **kwargs):
    '''Add revoew to product '''

    template_name = 'products/comment_product.html'
    model = testimonial
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # check form is valid and get values from it into variables.
            for arg in kwargs.values():
                article_id=arg
            body = comment_form.cleaned_data.get("body")
            comment_form.name_id=User.id
            
            # add new comment to database
            record = testimonial(name_id=request.user.id,body=body,approved=False,article_id=article_id)
            record.save()

            # notify the user
            messages.info(request, "Your review has been added.")
            messages.info(request, "It is awaiting approval.")

            # return to article comment was made on
            return HttpResponseRedirect("/products/"+str(article_id))
        else:
            comment_form = CommentForm()

    return render(
        request,
        "products/comment_product.html",
        {"form": comment_form},
    )