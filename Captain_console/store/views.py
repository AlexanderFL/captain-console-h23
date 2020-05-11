from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from store.models import Product, ProductDetails, ProductPhoto, Review, Developer
from account.models import User
import json
from django.forms.models import model_to_dict
from collections import OrderedDict
from store.store_forms.store_form import GiveRatingForm


def index(request):
    #User ordering products in store
    if 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']

        if sort_by == "price":
            products = Product.objects.all().order_by('price')

        elif sort_by == "name":
            products = Product.objects.all().order_by('name')

        elif sort_by == "rating":
            products = Product.objects.all().order_by('-average_rating')

        product_resp = [{
            'id': x.id,
            'name': x.name,
            # 'path': x.productphoto_set.first().path,
            # 'alt_val': x.productphoto_set.first().alt,
            # 'price': x.price,
            # 'discounted_price': x.get_discounted_price(),
            # 'discount': x.discount,
        } for x in products]

        return JsonResponse({'data': product_resp})

    if 'filter_by' in request.GET:
        print("hello")
        data = request.GET
        filter_by = data.get("filter_by")
        filter_var = data.get("filter_var")

        if filter_var =="All":  #Return all objects
            products = Product.objects.all()
            print("Yes")

        elif filter_by == "developer_filter":
            products = Product.objects.filter(productdetails__developer_id__developer__exact=filter_var)
            print(products)

        elif filter_by == "genre_filter":
            products = Product.objects.filter(productdetails__genre_id__genre__exact=filter_var)
            print(products)

        product_resp = [{
            'id': x.id,
            'name': x.name,
        } for x in products]

        return JsonResponse({'data': product_resp})

    #Initial load - order by name
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/index.html', context)


def games(request):
    print("hello")
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/games.html', context)


def consoles(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/consoles.html', context)


@csrf_exempt
def get_product_by_id(request, id):
    #Review product
    if 'review_product' in request.GET:
        #Extract data from jQuery dict
        data = request.POST
        prod_id = data.get("prod_id")
        rating = data.get("rating")

        #Get Product and User instances and create review
        product = get_object_or_404(Product, pk=prod_id)
        user = get_object_or_404(User, pk=1)
        new_review = Review()
        new_review.create_review(product, user, rating)

        print("Rating before: " + str(product.average_rating))

        #Update average rating for the product
        new_rating = product.get_rating()
        product.set_rating(new_rating, prod_id)

        print("Rating after: " + str(product.average_rating))
        return redirect('product_details', id=id)


    return render(request, 'store/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


def search(request, query):
    return render(request, 'store/search.html', {
        'search_results': get_list_or_404(Product.objects.filter(name__icontains=query)),
        'search_query': query
    })


   #
   # print(type(products))
   #          print(products)
   #
   #          products_sorted = {}
   #          for product in products:
   #              print(product.name)
   #              rating = product.get_rating()
   #              products_sorted[rating] = product
   #              print(product.get_rating())
   #
   #          sort_dict = {k: products_sorted[k] for k in sorted(products_sorted, reverse=True)}
   #
   #          print(type(sort_dict))
   #          print(sort_dict)
   #          products = []
   #          for k, v in sort_dict.items():
   #              print(k)
   #              print(v)
   #              products.append(v)
   #
   #          print(type(products))
   #          print(products)
   #          for product in products:
   #              print(product)
   #
   #          return JsonResponse({'data': products})