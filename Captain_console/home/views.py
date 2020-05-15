from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from account.models import User
from checkout.models import add_product_to_cart, Order, OrderProduct
from store.models import Product
from home.models import News
import json



def index(request):
    if 'add_to_cart' in request.GET:
        print("In add_to_cart")
        user_id = request.session.get('user_id')

        if user_id is None:
            response = json.dumps({'status': 999, 'message': '/login/register'})
            return HttpResponse(response, content_type='application/json')
        else:
            data = request.GET
            prod_id = data.get("prod_id")
            quantity = int(data.get("quantity"))
            print(quantity)
            print(prod_id)
            print("Quantity is" + str(quantity) + "and type" + str(type(quantity)))
            add_product_to_cart(prod_id, quantity, user_id)

            prod_list = []
            user = User.objects.get(pk=user_id)
            order = Order.objects.get(user_id=user, confirmed=False)
            order_products = OrderProduct.objects.filter(order_id=order)
            for x in order_products:
                prod_list.append({'qty': x.quantity, 'price': x.price, 'id': x.id})
            return JsonResponse({'data': prod_list})



    context = {'products': Product.objects.all()[:3], 'articles': News.objects.all().order_by('-date')[:3]}
    return render(request, 'home/index.html', context)


def terms(request):
    context = {'products': Product.objects.all()[:3]}
    return render(request, 'home/terms.html', context)


def aboutus(request):
    context = {'products': Product.objects.all()[:3]}
    return render(request, 'home/aboutus.html', context)


def logout(request):
    if request.session.__contains__('user_id'):
        request.session.pop('user_id')
    context = {'products': Product.objects.all()[:3]}
    return render(request, 'home/index.html', context)


def readmore(request, id):
    return render(request, 'home/article.html', {'article': News.objects.get(pk=id), 'articles': News.objects.all().order_by('-date')[:5]})

