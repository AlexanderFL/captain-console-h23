import json
from django.forms.models import model_to_dict
from collections import OrderedDict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from store.models import Product, ProductDetails, ProductPhoto, Review


def index(request):
    if 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']

        if sort_by == "price":
            products = Product.objects.order_by('price').values()
        elif sort_by == "name":
            products = Product.objects.order_by('name').values()
            print(list(products))
        elif sort_by == "rating":
            products = Product.objects.all()

            print(products)

            products_sorted = {}
            for product in products:
                print(product.name)
                rating = product.get_rating()
                products_sorted[rating] = product
                print(product.get_rating())

            sort_dict = {k: products_sorted[k] for k in sorted(products_sorted, reverse=True)}
            products = []
            for k, v in sort_dict.items():
                products.append(v)

            return JsonResponse({'data': products})

        print(products)
        return JsonResponse({'data': list(products)})

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
