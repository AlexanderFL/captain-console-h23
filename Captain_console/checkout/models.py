import random
from django.db import models
from account.models import User
from store.models import Product

'''
Checks if user has a non-confirmed order ("shopping cart")
'''


def active_order(user_id, product=None, quantity=None):
    empty_order = False
    orders = Order.objects.filter(user_id=user_id)

    for order in orders:
        if not order.confirmed:  # Shopping cart
            shopping_cart = order
            empty_order = True

    if not empty_order:  # No items in shopping cart, create non-confirmed order
        new_order = Order.objects.create(user_id=user_id, total_price=calculate_price(quantity, product))
        shopping_cart = new_order
    return shopping_cart


'''
Checks how many items user has in cart. Deletes oreder if empty
'''


def number_of_items_in_cart(owner):
    order_products = OrderProduct.objects.filter(user_id=owner, order_id__confirmed=False)
    items_in_cart = len(order_products)
    return items_in_cart


'''
Deletes active order
'''


def delete_active_order(owner):
    Order.objects.filter(user_id=owner, confirmed=False).delete()


'''
Checks if product is already in cart. Returns order_product object if product is in cart. Else returns False.
'''


def check_if_already_in_cart(user_id, product):
    order_products = OrderProduct.objects.filter(user_id=user_id, order_id__confirmed=False)
    for order_product in order_products:
        if order_product.product_id.id == product.id:
            return order_product
    return False


'''
Price calculated
'''


def calculate_price(quantity, product):
    total_price = product.price * quantity * (100 - product.discount) / 100
    return "{:.2f}".format(total_price)


'''
Removes item from cart. If last item removed - delete open order.
'''


def remove_product_from_cart(orderprod_id):
    order_product = OrderProduct.objects.get(pk=orderprod_id, order_id__confirmed=False)
    owner = order_product.user_id
    order_product.delete()

    qty_in_cart = number_of_items_in_cart(owner)

    if qty_in_cart == 0:
        delete_active_order(owner)


'''
Updates product in cart
'''


def update_product_in_cart(order_product, new_quantity):
    total_price = calculate_price(new_quantity, order_product.product_id)
    OrderProduct.objects.filter(pk=order_product.id, order_id__confirmed=False).update(quantity=new_quantity, price=total_price)


'''
Creates a new order_product in cart
'''


def create_product_in_cart(product, quantity, user, shopping_cart):
    total_price = calculate_price(quantity, product)
    OrderProduct.objects.create(product_id=product, quantity=quantity, price=total_price, user_id=user,
                                order_id=shopping_cart)


'''
Adds product to cart or updates quantity if already in cart
'''


def add_product_to_cart(product_id, quantity, user_id):
    user = User.objects.get(pk=user_id)
    product = Product.objects.get(pk=product_id)

    # Get order id for active non-confirmed order
    shopping_cart = active_order(user, product, quantity)

    # Check if item is in cart
    in_cart = check_if_already_in_cart(user_id, product)

    if not in_cart:
        create_product_in_cart(product, quantity, user, shopping_cart)
    else:
        new_quantity = in_cart.quantity + quantity
        update_product_in_cart(in_cart, new_quantity)


'''
Add to or subtract item in cart
'''


def change_qty(orderprod_id, change_type):
    order_product = OrderProduct.objects.get(pk=orderprod_id, order_id__confirmed=False)
    order_product_quantity = order_product.quantity

    if change_type == "add":
        new_quantity = order_product.quantity + 1
    else:
        if order_product_quantity == 1:
            return
        new_quantity = order_product.quantity - 1
    update_product_in_cart(order_product, new_quantity)
    return new_quantity


'''
Get shipping address
'''

def get_track_number():
    return str(random.randrange(1000000000, 9999999999))


'''
Mark order confirmed
'''


def mark_order_confirmed(user):
    track_number = get_track_number()
    Order.objects.filter(user_id=user, confirmed=False).update(confirmed=True, tracking_nr=track_number)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    tracking_nr = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)


class OrderProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
