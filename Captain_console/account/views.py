from django.shortcuts import render
from account.models import User, PaymentInfo, Address, UserPhoto
from store.models import OrderProduct, Product, ProductPhoto, Order


#
# 'SELECT product_id_id FROM store_orderproduct WHERE order_id_id in (SELECT id FROM store_order WHERE user_id_id = %s',[id])

def base_context(id, context):
    query_user = User.objects.get(pk=id)

    query_order_history = Order.objects.filter(user_id=id)[:3]
    query_order = query_user.order_set.all().order_by('-date')[:3]
    # query_order_history = Order.objects.raw('SELECT * FROM store_order WHERE user_id_id = %s LIMIT 3', [id])

    # query_test = OrderProduct.objects.raw('SELECT product_id_id FROM store_orderproduct WHERE order_id_id in (SELECT id FROM store_order WHERE user_id_id = %s)',[id])

    context['user'] = query_user
    context['orders'] = query_order_history
    # context['orders'] = product_details
    # context['test'] = query_test
    context['order'] = query_order

    # : OrderProduct.objects.get()

    context['user'] = User.objects.get(pk=id)

    return context


def index(request, id):
    context = {
        'page_account': 'profile',
    }
    if id != None:
        context = base_context(id, context)
    return render(request, 'account/index.html', context)

def edit(request, id):
    context = {
        'page_account': 'edit_profile',
    }
    if id != None:
        context = base_context(id, context)
    return render(request, 'account/index.html', context)

