from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from store.models import Product, ProductDetails, ProductPhoto, Review, Developer, Genre, Category, write_review
from account.models import User
from checkout.models import OrderProduct, add_product_to_cart, Order
import json
from django.db.models import F, Func


@csrf_exempt
def index(request):
    context = {}
    context['developers'] = Developer.objects.all()
    context['genres'] = Genre.objects.all()
    context['categories'] = Category.objects.all()

    print("hello1")
    print(request.POST)
    # Add to cart

    if 'add_to_cart' in request.GET:
        print("In add_to_cart")
        user_id = request.session.get('user_id')

        if user_id is None:
            response = json.dumps({'status': 999, 'message': '/login/register'})
            return HttpResponse(response, content_type='application/json')

        else:
            # Get data from post request
            data = request.POST
            prod_id = data.get("prod_id")
            quantity = int(data.get("quantity"))
            print("Quantity is" + str(quantity) + "and type" + str(type(quantity)))
            # Create a new instance of order product and add to cart
            add_product_to_cart(prod_id, quantity, user_id)

            prod_list = []
            user = User.objects.get(pk=user_id)
            order = Order.objects.get(user_id=user, confirmed=False)
            order_products = OrderProduct.objects.filter(order_id=order)
            for x in order_products:
                prod_list.append({'qty': x.quantity, 'price': x.price, 'id': x.id})
            return JsonResponse({'data': prod_list})

    # Search
    if 'search_by' in request.GET:
        search_by = request.GET['search_by']
        products = Product.objects.filter(name__icontains=search_by)
        print("Search by: {}".format(search_by))

        prod_list = []
        for x in products:
            prod_list.append({'id': x.id})
        return JsonResponse({'data': prod_list})

    # Sort by price, name or rating
    elif 'sort_by' in request.GET:
        sort_by = request.GET['sort_by']

        if sort_by == "price":
            products = Product.objects.all().order_by(F('price') * (100 - F('discount')) / 100)
        elif sort_by == "name":
            products = Product.objects.all().order_by('name')
        elif sort_by == "rating":
            products = Product.objects.all().order_by('-average_rating')

        prod_list = []
        for x in products:
            prod_list.append({'id': x.id, 'name': x.name})
        return JsonResponse({'data': prod_list})


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

        prod_list = []
        for x in filtered_products:
            prod_list.append({'id': x.id})
        return JsonResponse({'data': prod_list})

    # Initial Store load - order by name
    context['products'] = Product.objects.all().order_by('name')
    return render(request, 'store/index.html', context)


@csrf_exempt
# Get product details
def get_product_by_id(request, id):
    # Review product
    if 'review_product' in request.GET:
        new_review = Review()
        data = request.POST
        prod_id = data.get("prod_id")
        product = get_object_or_404(Product, pk=prod_id)
        rating = data.get("rating")

        if request.session.__contains__('user_id'):
            user_id = request.session.get('user_id')
            user = User.objects.get(pk=user_id)
            new_review.create_review(product, rating, user_id)

        else:
            new_review.create_review(product, rating, 1)

        # Update average rating for the product
        new_rating = product.get_rating()
        product.set_rating(new_rating, prod_id)
        return redirect('product_details', id=id)

    amount = 0
    copies_sold = OrderProduct.objects.filter(product_id=id)
    for copy in copies_sold:
        amount += copy.quantity

    return render(request, 'store/product_details.html', {
        'product': get_object_or_404(Product, pk=id),
        'copies_sold': amount
    })


def reviews(request, id):

    if "review_product" in request.GET:
        data = request.GET
        user_id = request.session.get("user_id")
        prod_id = data.get("prod_id")
        comment = data.get("comment")
        stars = data.get("stars")

        rating = write_review(prod_id, user_id, comment, stars)

        if rating == "Rating updated":
            response = json.dumps({'status': 999, 'message': 'Updated'})
            print("Rating updated")
        else:
            response = json.dumps({'status': 200, 'message': 'Created'})
            print("Rating created")
        return HttpResponse(response, content_type='application/json')


    context = {}
    context['reviews'] = Review.objects.exclude(comment__exact="").filter(product_id=id).order_by("rating")
    context['product'] = Product.objects.get(pk=id)
    return render(request, 'store/reviews.html', context)
