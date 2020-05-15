import json

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from account.models import User, PaymentInfo, Address, UserPhoto
from store.models import Product, ProductPhoto
from checkout.models import OrderProduct, Order



def base_context(id, context):

    context['user'] = User.objects.get(pk=id)

    query_order = Order.objects.filter(user_id=id, confirmed=True).order_by('-id')[:3]
    query_list = []
    if query_order != None :
        for order in query_order:
            if order != None:
                query_list.append(order.id)

        print("Query_list: {}".format(query_list))

        query_products = Product.objects.filter(orderproduct__order_id_id__in=[19])

        if query_products.count() > 0 :
            print("query_products.count() er: {}".format(query_products.count()))
            counter = 0
            for i, value in enumerate(query_products) :
                # print("i is: {}, and value is: {}".format(i, value))
                # print("query_products[i] is: {}".format(query_products[i]))
                query_orderproduct = OrderProduct.objects.filter(order_id_id=query_order[i].id)

                if len(query_orderproduct) > 1 :
                    #
                    # query_copy = copy.deepcopy(query_order[i])
                    #
                    # for dic in query_orderproduct :
                    #     photo_query = ProductPhoto.objects.get(product_id_id=value.id)
                    #
                    #     query_copy.quantity = query_orderproduct.quantity
                    #     query_copy.path = photo_query.path
                    #     query_copy.alt = photo_query.alt
                    #     query_copy.name = value.name
                    #     query_copy.photo = value.productphoto_set.name
                    #     query_copy.rating = value.average_rating
                    #
                    # deep = copy.deepcopy()
                    #
                    #

                    new_dict = {}
                    for j, orderproducts in enumerate(query_orderproduct) :



                        photo_query = ProductPhoto.objects.filter(product_id_id=orderproducts.product_id_id)

                        print("photo_query: {}".format(photo_query))
                        for p in photo_query :
                            print("p in photoquery: {}".format(photo_query))

                            new_dict = { j: {
                                    'quantity': orderproducts.quantity,
                                    'path':  p.path,
                                    'alt': p.alt,
                                    'name': value.name,
                                    'photo': value.productphoto_set.name,
                                    'rating': value.average_rating,
                                }
                            }

                    query_order[i].many = new_dict
                    print("Needs debugging")

                else :
                    for each in query_orderproduct : # should only have 1 anyways
                        print("Hingað")
                        photo_query = ProductPhoto.objects.get(product_id_id=value.id)

                        query_order[i].quantity = each.quantity

                        query_order[i].path = photo_query.path
                        query_order[i].alt = photo_query.alt
                        query_order[i].name = value.name
                        query_order[i].photo = value.productphoto_set.name
                        query_order[i].rating = value.average_rating
                        print("og ekki lengra")
        context['orders'] = query_order

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