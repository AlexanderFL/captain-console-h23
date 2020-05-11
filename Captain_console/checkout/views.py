from django.shortcuts import render
from account.models import User
from store.models import Product

# Create your views here.

def base_context(id, context):
    context['user'] = User.objects.get(pk=id)
    context['product'] = Product.objects.raw('SELECT * FROM store_product, store_orderproduct, store_order WHERE store_product.id = store_orderproduct.product_id_id  AND store_orderproduct.order_id_id = store_order.id  AND store_order.user_id_id = s%;', [id])
    return context


 # products = Product.objects.filter(orderproduct__order_id__user_id=id)

def index(request, id=None):
    context = {
        'page_checkout': 'contactinfo',
    }
    if id != None:
        context = base_context(id, context)
    return render(request, 'checkout/index.html', context)

def shipping(request, id=None):
    context = {
        'page_checkout': 'shipping',
    }
    if id != None:
        context = base_context(id, context)
    return render(request, 'checkout/index.html', context)

def payment(request, id=None):
    context = {
        'page_checkout': 'paymentinfo',
    }
    if id != None:
        context = base_context(id, context)
    return render(request, 'checkout/index.html', context)

def confirmation(request, id=None):
    context = {
        'page_checkout': 'confirmation',
    }
    if id != None:
        context = base_context(id, context)
    return render(request, 'checkout/index.html', context)

