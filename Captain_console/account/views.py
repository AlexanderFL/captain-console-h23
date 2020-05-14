import json

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.models import User, PaymentInfo, Address, UserPhoto
from store.models import Product, ProductPhoto
from checkout.models import OrderProduct, Order


#
# 'SELECT product_id_id FROM store_orderproduct WHERE order_id_id in (SELECT id FROM store_order WHERE user_id_id = %s',[id])

def base_context(id, context):
    print(id)
    query_user = User.objects.get(pk=id)

    #query_order_history = OrderProduct.objects.filter(user_id=id)[:3]
    query_order = query_user.order_set.all().order_by('-id')[:3]
    # query_order_history = Order.objects.raw('SELECT * FROM store_order WHERE user_id_id = %s LIMIT 3', [id])

    # query_test = OrderProduct.objects.raw('SELECT product_id_id FROM store_orderproduct WHERE order_id_id in (SELECT id FROM store_order WHERE user_id_id = %s)',[id])

    context['user'] = query_user
    #context['orders'] = query_order_history
    # context['orders'] = product_details
    # context['test'] = query_test
    context['order'] = query_order

    # : OrderProduct.objects.get()

    context['user'] = User.objects.get(pk=id)

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
        print("account/views.py: I'm exectued")
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

                response = json.dumps({'status': 200, 'message': 'http://localhost:8000/account/'})
                return HttpResponse(response, content_type='application/json')
        else:
            context = {
                'page_account': 'edit_profile',
            }
            context = base_context(user_id, context)
            return render(request, 'account/index.html', context)
    else:
        return render(request, 'login/index.html', context={'page_login': 'login_index'})