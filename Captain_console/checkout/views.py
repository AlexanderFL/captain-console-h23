import json
from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from account.models import User, PaymentInfo
from store.models import Product
from checkout.models import Order, OrderProduct, remove_product_from_cart


# Base functions for all checkout views
def base_context(user_id):
    user = User.objects.get(pk=user_id)
    order_products = OrderProduct.objects.filter(order_id__user_id=user_id)

    context = {
        'user': user,
        'order_products': order_products,
    }
    return context


def base_remove_from_cart(request):
    print(request.GET)
    order_prod_id = request.GET['remove_from_cart']
    print("this is prod-id" + str(order_prod_id))
    order_product = OrderProduct()
    remove_product_from_cart(order_prod_id)

    product_resp = [{
        'order_prod_id': order_prod_id
    }]
    return JsonResponse({'data': product_resp})


def base_change_qty_of_prod(request):
    order_prod_id = request.GET['order_prod_id']
    change_type = request.GET['change_type']
    order_product = OrderProduct()
    new_quantity = order_product.change_qty(order_prod_id, change_type)

    product_resp = [{
        'new_qty': new_quantity
    }]
    return JsonResponse({'new_quantity': product_resp})


@csrf_exempt
def index(request):
    # If user is not logged in - render login page
    user_id = request.session.get("user_id")
    if user_id is None:
        return render(request, 'login/index.html')

    # Base context
    context = base_context(user_id)

    # Specific context
    context['page_checkout'] = 'contactinfo'

    # Change qty of item in cart
    if 'change_qty' in request.GET:
        return base_change_qty_of_prod(request)

    # Remove item from cart
    if 'remove_from_cart' in request.GET:
        return base_remove_from_cart(request)

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

    # Change qty of item in cart
    if 'change_qty' in request.GET:
        return base_change_qty_of_prod(request)

    # Remove item from cart
    if 'remove_from_cart' in request.GET:
        return base_remove_from_cart(request)

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

    # Change qty of item in cart
    if 'change_qty' in request.GET:
        return base_change_qty_of_prod(request)

    # Remove item from cart
    if 'remove_from_cart' in request.GET:
        return base_remove_from_cart(request)

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
