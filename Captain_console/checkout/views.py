import json
from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from account.models import User, PaymentInfo
from store.models import Product
from checkout.models import Order, OrderProduct


def base_context(user_id):
    user = User.objects.get(pk=user_id)
    print("hello")
    order_products = OrderProduct.objects.filter(order_id__user_id=user_id)

    context = {
        'user': user,
        'order_products': order_products,
    }
    return context


@csrf_exempt
def index(request):

    # If user is not logged in - render login page
    user_id = request.session.get("user_id")
    print(user_id)
    print(type(user_id))
    if user_id is None:
        return render(request, 'login/index.html')

    # Base context
    context = base_context(user_id)

    # Specific context
    context['page_checkout'] = 'contactinfo'

    # Add item to cart
    data = request.POST
    "hello2"
    if "add_item" in request.GET:
        prod_id = data.get("order_prod_id")
        order_product = OrderProduct()
        order_product.add_item(prod_id)

    # Remove item from cart
    if 'remove_from_cart' in request.GET:
        print(request.GET)
        order_prod_id = request.GET['remove_from_cart']

        print("this is prod-id" + str(order_prod_id))
        order_product = OrderProduct()
        order_product.remove_product_from_cart(order_prod_id)
        return JsonResponse({'data': order_prod_id})

    return render(request, 'checkout/index.html', context)


def shipping(request, id=None):
    # If user is not logged in - render login page
    user_id = request.session.get("user_id")
    if user_id is None:
        return render(request, 'login/index.html')

    # Base context
    context = base_context(user_id)

    # Specific context
    context['page_checkout'] = "shipping"

    return render(request, 'checkout/index.html', context)


@csrf_exempt
def payment(request, id=None):
    # If user is not logged in - render login page
    user_id = request.session.get("user_id")
    if user_id is None:
        return render(request, 'login/index.html')

    # Base context
    context = base_context(user_id)

    # Specific context
    context['page_checkout'] = "paymentinfo"

    if request.method == 'POST':
        # Make sure user is logged in
        if request.session.get('user_id') is None:
            response = json.dumps({'status': 999, 'message': 'User not logged in'})
            return HttpResponse(response, content_type='application/json')

        cardHolder = request.POST.get('cardHolder')
        cardNumber = request.POST.get('cardNumber')
        expireDate = request.POST.get('expireDate')
        cvc = request.POST.get('cvc')

        PaymentInfo.insert(User.objects.get(pk=request.session.get('user_id')), cardHolder, cardNumber, expireDate, cvc)

        response = json.dumps({'status': 200, 'message': 'Yes'})
        return HttpResponse(response, content_type='application/json')

    return render(request, 'checkout/index.html', context)


def confirmation(request):
    user_id = request.session.get("user_id")
    if user_id is None:
        return render(request, 'login/index.html')

    context = {
        'page_checkout': 'confirmation',
    }

    context = base_context(user_id, context)
    return render(request, 'checkout/index.html', context)
