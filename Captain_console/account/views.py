import json, bcrypt
from copy import deepcopy
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.models import User, PaymentInfo, Address, UserPhoto
from store.models import Product, ProductPhoto
from checkout.models import OrderProduct, Order


def base_context(id, context):

    context['user'] = User.objects.get(pk=id)
    query_order = OrderProduct.objects.filter(user_id=id, order_id__confirmed=True).order_by('-order_id__date', 'order_id_id')

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

        if request.method == "POST":
            current_password = request.POST.get('current_password').encode('utf-8')
            new_password = request.POST.get('new_password').encode('utf-8')
            stored_password = User.get_password_from_id(user_id)

            hashed_pass = stored_password.encode('utf-8')
            if bcrypt.checkpw(current_password, hashed_pass):
                new_password_hash = bcrypt.hashpw(new_password, bcrypt.gensalt())
                new_password_hash = new_password_hash.decode('utf-8')
                User.update_user_password(user_id, new_password_hash)

                response = json.dumps({'status': 200, 'message': '/account/'})
                return HttpResponse(response, content_type='application/json')
            else:
                response = json.dumps({'status': 0, 'message': 'Incorrect password'})
                return HttpResponse(response, content_type='application/json')
        context = {
            'user': User.objects.get(pk=user_id)
        }
        return render(request, 'account/change_password.html', context)
    else:
        return render(request, 'login/index.html', context={'page_login': 'login_index'})