from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from store.models import Product, ProductDetails, ProductPhoto


def index(request):
    if 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']
        products = list(Product.objects.order_by('price'))
        print(products)
        return JsonResponse({'data': products})

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
        'product': get_object_or_404(Product, pk=id)
    })


def search(request, query):
    return render(request, 'store/search.html', {
        'search_results': get_list_or_404(ProductPhoto.objects.filter(product_id__name__icontains=query)),
        'search_query': query
    })