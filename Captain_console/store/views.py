from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from store.models import Product, ProductDetails, ProductPhoto, Review, Developer

from account.models import User
from checkout.models import OrderProduct
import json


def index(request):
    # Search
    if 'search_by' in request.GET:
        search_by = request.GET['search_by']
        products = Product.objects.filter(name__icontains=search_by)

        product_resp = [{
            'id': x.id
        } for x in products]
        return JsonResponse({'data': product_resp})

    # Sort by price, name or rating
    elif 'sort_by' in request.GET:
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
        } for x in products]
        return JsonResponse({'data': product_resp})

    # Filter applications
    elif 'filter_by' in request.GET:
        data = request.GET
        developer = data.get("developer")
        genre = data.get("genre")
        category = data.get("category")

        # Developer filter - get all products by filter
        if (developer == "All") or (developer == "Developer"):
            dev_products = Product.objects.all()
        else:
            dev_products = Product.objects.filter(productdetails__developer_id__developer__exact=developer)

        # Genre filter - get all products by filter
        if (genre == "All") or (genre == "Genre"):
            genre_products = Product.objects.all()
        else:
            genre_products = Product.objects.filter(productdetails__genre_id__genre__exact=genre)

        # Category filter - get all products by filter
        if (category == "All") or (category == "Category"):
            cat_products = Product.objects.all()
        else:
            cat_products = Product.objects.filter(category__name__exact=category)

        # Find the union of filtered items and return
        filtered_products = dev_products & genre_products & cat_products
        product_resp = [{
            'id': x.id,
        } for x in filtered_products]
        return JsonResponse({'data': product_resp})

    # Add to cart
    elif 'add_to_cart' in request.POST:
        data = request.POST
        user_id = request.session.get('user_id')
        order_product = OrderProduct()

    # Initial Store load - order by name
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/index.html', context)


# Get product details
@csrf_exempt
def get_product_by_id(request, id):
    if 'copies_sold' in request.GET:
        copies_sold = OrderProduct.objects.filter(product_id=id).count()
        response = json.dumps({'status': 200, 'message': copies_sold})
        return HttpResponse(response, content_type='application/json')

    # Review product
    if 'review_product' in request.GET:
        data = request.POST
        prod_id = data.get("prod_id")
        rating = data.get("rating")
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)

        # Get Product and User instances and create review
        product = get_object_or_404(Product, pk=prod_id)
        new_review = Review()
        new_review.create_review(product, user, rating)

        # Update average rating for the product
        new_rating = product.get_rating()
        product.set_rating(new_rating, prod_id)
        return redirect('product_details', id=id)

    return render(request, 'store/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


# Dynamic search in store
def search(request, query):
    return render(request, 'store/search.html', {
        'search_results': get_list_or_404(Product.objects.filter(name__icontains=query)),
        'search_query': query
    })
