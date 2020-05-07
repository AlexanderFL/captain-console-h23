from django.shortcuts import render
from account.models import User, PaymentInfo, Address, UserPhoto
from store.models import OrderProduct, Product, ProductPhoto




def index(request, id):
    context = {
        'user': User.objects.get(pk=id),
        'photo': UserPhoto.objects.get(user_id=id)
    }
    return render(request, 'account/index.html', context)




    #        'user': get_object_or_404(User, pk=id)
    # account = {
    #     'user': User.objects.filter(id=user_id)
    # }
    # order = {
    #     'order_history': OrderProduct.objects.filter(account.id)
    # }

    # context = {
    #     'user': User.objects.get(id=user_id)
        # 'user': User.objects.filter(id=userid)
        # 'payment': PaymentInfo.objects.filter(account.id),
        # 'address': Address.objects.filter(account.id),
        # 'user_photo': UserPhoto.objects.filter(account.id),
        # 'order_history': OrderProduct.objects.filter(account.id),
#        'product': Product.objects.filter(order.order_history.prouct_id_id)
#        'product_photo': ProductPhoto.objects.filter(order)
#     }
#
#
#     return render(request, 'account/index.html', context)

