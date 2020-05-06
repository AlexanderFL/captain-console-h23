from django.shortcuts import render, get_object_or_404
from store.models import Product, ProductDetails


def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/index.html', context)


def games(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/games.html', context)


def consoles(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/consoles.html', context)


def get_product_by_id(request, id):
    return render(request, 'store/product_details.html', {
        'productdetails': get_object_or_404(ProductDetails, pk=id)
    })
