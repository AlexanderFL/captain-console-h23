from django.shortcuts import render
from account.models import User, PaymentInfo, Address, UserPhoto
from store.models import OrderProduct, Product, ProductPhoto, Order


#
# 'SELECT product_id_id FROM store_orderproduct WHERE order_id_id in (SELECT id FROM store_order WHERE user_id_id = %s',[id])

def index(request, id):
    query_user = User.objects.get(pk=id)

    query_order_history = Order.objects.filter(user_id=id)[:3]
    # query_order_history = Order.objects.raw('SELECT * FROM store_order WHERE user_id_id = %s LIMIT 3', [id])

    # query_test = OrderProduct.objects.raw('SELECT product_id_id FROM store_orderproduct WHERE order_id_id in (SELECT id FROM store_order WHERE user_id_id = %s)',[id])
    query_address = query_user.address_set.all()


    context = {
        'user': query_user,
        'page_account': 'profile',
        'orders': query_order_history,
        # 'orders': product_details,
        # 'test': query_test,
        'address': query_address,

        # : OrderProduct.objects.get()
    }

    return render(request, 'account/index.html', context)

def edit(request, id):
    context = {
        'user': User.objects.get(pk=id),
        # 'address': Address.objects.filter(user_id.id),
        'page_account': 'edit_profile'
    }
    return render(request, 'account/index.html', context)

