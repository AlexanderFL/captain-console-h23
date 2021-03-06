import json
from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from account.models import User, PaymentInfo
from store.models import Product
from checkout.models import OrderProduct, remove_product_from_cart, change_qty, mark_order_confirmed, Order, number_of_items_in_cart


# Base functions for all checkout views
def base_context(user_id):
    user = User.objects.get(pk=user_id)
    order_products = OrderProduct.objects.filter(order_id__user_id=user_id, order_id__confirmed=False)

    total_price = 0
    if len(order_products) > 0:
        for order_product in order_products:
            total_price += order_product.price
        total_price =  "{:.2f}".format(total_price)
        total_price = "Subtotal: $" + str(total_price)
    else:
        total_price = "Your cart is empty. Feel free to go to store to start shopping."

    context = {
        'user': user,
        'order_products': order_products,
        'total_price': total_price,
    }
    return context


def base_remove_from_cart(request):
    print(request.GET)
    order_prod_id = request.GET['remove_from_cart']
    print("this is prod-id" + str(order_prod_id))
    remove_product_from_cart(order_prod_id)

    user_id = request.session.get("user_id")
    user = User.objects.get(pk=user_id)
    try:
        prod_list = []
        order = Order.objects.get(user_id=user, confirmed=False)
        order_products = OrderProduct.objects.filter(order_id=order)
        for x in order_products:
            prod_list.append({'qty': x.quantity, 'price': x.price, 'id': x.id})
        return JsonResponse({'data': prod_list})
    except:
        prod_list = []
        return JsonResponse({'data': prod_list})


def base_change_qty_of_prod(request):
    order_prod_id = request.GET['order_prod_id']
    change_type = request.GET['change_type']
    change_qty(order_prod_id, change_type)

    user_id = request.session.get("user_id")
    user = User.objects.get(pk=user_id)
    print(user_id)

    order = Order.objects.get(user_id=user, confirmed=False)
    print(order.id)
    order_products = OrderProduct.objects.filter(order_id=order)

    prod_list = []
    for x in order_products:
        prod_list.append({'qty': x.quantity, 'price': x.price, 'id': x.id})
    return JsonResponse({'data': prod_list})


@csrf_exempt
def index(request):
    if request.method == "GET":
        try:
            navbar_request = request.GET['navbar']
            response_message = number_of_items_in_cart(request.session['user_id'])
            response = json.dumps({'status': 200, 'message': response_message})
            return HttpResponse(response, content_type='application/json')
        except Exception:
            pass
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

    if 'check_cart' in request.GET:
        order_products = OrderProduct.objects.filter(user_id=user_id, order_id__confirmed=False)

        if len(order_products) == 0:
            response = json.dumps({'status': 999, 'message': 'empty'})
            print("no items in cart")
        else:
            response = json.dumps({'status': 200, 'message': 'not_empty'})
            print("items in cart")
        return HttpResponse(response, content_type='application/json')

    # Change qty of item in cart
    if 'change_qty' in request.GET:
        return base_change_qty_of_prod(request)

    # Remove item from cart
    if 'remove_from_cart' in request.GET:
        return base_remove_from_cart(request)

    if 'save_card' in request.GET:
        print("saving card")

        cardHolder = request.POST.get('cardHolder')
        cardNumber = request.POST.get('cardNumber')
        expireDate = request.POST.get('expireDate')
        cvc = request.POST.get('cvc')

        PaymentInfo.insert(User.objects.get(pk=request.session.get('user_id')), cardHolder, cardNumber, expireDate, cvc)

        response = json.dumps({'status': 200, 'message': 'Yes'})
        return HttpResponse(response, content_type='application/json')

    if 'confirmed' in request.GET:
        print("confirming")
        user = request.session.get('user_id')
        print(user)
        mark_order_confirmed(user)
        print("order confirmed")
        response = json.dumps({'status': 200, 'message': '/checkout/confirmation'})
        return HttpResponse(response, content_type='application/json')
    return render(request, 'checkout/index.html', context)


def confirmation(request):
    user_id = request.session.get("user_id")

    # Base context
    context = base_context(user_id)

    # Specific context
    context['page_checkout'] = 'confirmation'
    context['order'] = Order.objects.filter(user_id=user_id).order_by('-id')[0]

    print(context)
    return render(request, 'checkout/index.html', context)
