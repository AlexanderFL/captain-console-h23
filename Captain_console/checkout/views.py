import json
from itertools import chain
from django.http import HttpResponse
from django.shortcuts import render
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

    #If user is not logged in - render login page
    user_id = request.session.get("user_id")
    print(user_id)
    print(type(user_id))
    if user_id is None:
        return render(request, 'login/index.html')

    #Base context
    context = base_context(user_id)

    #Specific context
    context['page_checkout'] ='contactinfo'

    #Add item to cart
    data = request.POST
    if "add_item" in request.GET:
        prod_id = data.get("prod")
        print(prod_id)
        order_product = OrderProduct()
        order_product.add_item(prod_id)

    print(context)
    return render(request, 'checkout/index.html', context)


def shipping(request, id=None):
    user_id = request.session.get("user_id")
    if user_id is None:
        return render(request, 'login/index.html')

    #Base context
    context = base_context(user_id)

    #Specific context
    context['page_checkout'] = "shipping"

    return render(request, 'checkout/index.html', context)


@csrf_exempt
def payment(request, id=None):
    user_id = request.session.get("user_id")
    if user_id is None:
        return render(request, 'login/index.html')

    # Base context
    context = base_context(user_id)

    #Specific context
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



    # Þetta er vitlaust, þarf að pulla order_id úr order_product og matcha við þetta
    # Eins og er, er þetta allavega einhver data fyrir shoppingcart

  # if len(context['order_products']) > 1 :
    #     for order in context['order_products'] :
    #         p = Product.objects.get(pk=order.product_id)

    # u = User.objects.get(pk=id)
    # p = Order.objects.get('user_id_id'=id)
    # d = Product.objects.all()
    # o = Order.objects.all(user_id=1)

    # o = Order.objects.filter(user_id_id=1)
    # op = OrderProduct.objects.exclude(o.order_id_id)