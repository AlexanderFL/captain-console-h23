import json
from copy import deepcopy
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.models import User, PaymentInfo, Address, UserPhoto
from store.models import Product, ProductPhoto
from checkout.models import OrderProduct, Order



def base_context(id, context):

    context['user'] = User.objects.get(pk=id)

    query_order = OrderProduct.objects.filter(user_id=id, order_id__confirmed=True).order_by('order_id__date', 'order_id_id')

    query_list = []
    if query_order != None:
        for order in query_order:

            prod_ = Product.objects.get(pk=order.product_id_id)
            prod_photo = ProductPhoto.objects.get(product_id_id=order.product_id_id)
            prod_.photo = prod_photo

            order_ = Order.objects.get(pk=order.order_id_id)

            query_list.append({
                'id': order_.id,
                'price': order_.total_price,
                'tracking_nr': order_.tracking_nr,
                'date': order_.date,
                'products': {
                    'photo': prod_.photo.path,
                    'alt': prod_.photo.alt,
                    'name': prod_.name,
                    'rating': prod_.average_rating,
                    'id': prod_.id,
                    'quantity': order.quantity,
                }
            })

        context['orders'] = query_list

########################## DEBUGGING ########################
        #
        # for p in context['orders'] :
        #     print(p)
            # print(prod_.photo.path)
            # print(prod_.name)
            # print(prod_.average_rating)
            # print(prod_.id)
            #
            # print(order.quantity)
            #
            # print(order_.total_price)
            # print(order_.tracking_nr)
            # print(order_.date)
##########################################################



########################## OLD ########################

    # query_order = Order.objects.filter(user_id=id, confirmed=True).order_by('-id')[:3]
    # query_list = []
    # if query_order != None :
    #     for order in query_order:
    #         if order != None:
    #             query_list.append(order.id)
    #
    #     query_products = Product.objects.filter(orderproduct__order_id_id__in=query_list)
    #
    #     if len(query_products) > 0 :
    #         for i, value in enumerate(query_products) :
    #             # print("i is: {}, and value is: {}".format(i, value))
    #             # print("query_products[i] is: {}".format(query_products[i]))
    #
    #             photo_query = ProductPhoto.objects.get(product_id_id=value.id)
    #             query_orderproduct = OrderProduct.objects.get(order_id_id=query_order[i].id)
    #
    #             query_order[i].quantity = query_orderproduct.quantity
    #             query_order[i].path = photo_query.path
    #             query_order[i].alt = photo_query.alt
    #             query_order[i].name = value.name
    #             query_order[i].photo = value.productphoto_set.name
    #             query_order[i].rating = value.average_rating
    #
    #     context['orders'] = query_order
    ###########################################################

    return context


@csrf_exempt
def index(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        context = {
            'page_account': 'profile',
        }
        context = base_context(user_id, context)
        return render(request, 'account/index.html', context)
    else:
        return render(request, 'login/index.html', context={'page_login': 'login_index'})


@csrf_exempt
def edit(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        if request.method == "POST":
            email = str(request.POST.get("email")).lower()
            address = request.POST.get("address")
            country = request.POST.get("country")
            city = request.POST.get("city")
            a_zip = request.POST.get("zip")
            photo_url = request.POST.get('picture')

            not_same_email = True

            # If the email stored in database is the same as entered
            if User.objects.get(id=user_id).email == email:
                not_same_email = False

            # If the email is already in use by another account
            if User.email_already_exists(email) and not_same_email:
                response = json.dumps({'status': 0, 'message': 'Email already in use by another account'})
                return HttpResponse(response, content_type='application/json')
            else:
                if not_same_email:
                    User.objects.filter(id=user_id).update(email=email)
                Address.insert(User.objects.get(id=user_id), address, city, country, a_zip)

                if photo_url != "":
                    UserPhoto.update_photo(user_id, photo_url)

                response = json.dumps({'status': 200, 'message': '/account/'})
                return HttpResponse(response, content_type='application/json')
        else:
            context = {
                'page_account': 'edit_profile',
            }
            context = base_context(user_id, context)
            return render(request, 'account/index.html', context)
    else:
        return render(request, 'login/index.html', context={'page_login': 'login_index'})


@csrf_exempt
def change_password(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        context = {
            'user': User.objects.get(pk=user_id)
        }
        return render(request, 'account/change_password.html', context)
    else:
        return render(request, 'login/index.html', context={'page_login': 'login_index'})