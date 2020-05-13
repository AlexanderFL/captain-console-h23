from django.db import models
from account.models import User
from store.models import Product


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
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    # Creates new order product in DB
    def add_product_to_cart(self, product_id, quantity, user_id=None):

        # orders = Order.objects.get(pk=user_id)
        #
        # orders = Order.objects.get(pk=user_id)
        # print(orders)
        #
        # for order in orders:
        #     if order.order_id != 10:
        #         order.delete(confirmed=True)
        #
        # for order in orders:
        #     status = order.confirmed
        #     if status == False:
        #          shopping_cart = order
        #
        #     else:
        #          Order.objects.create()


        product = Product.objects.get(pk=product_id)
        user = User.objects.get(pk=user_id)
        total_price = product.price * quantity * (100 - product.discount) / 100
        OrderProduct.objects.create(product_id=product, quantity=quantity, price=total_price, user_id=user)

    # Increase quantity of item in cart
    def add_item(self, prod_id):
        print(prod_id)
        order_product = Product.objects.get(pk=prod_id)
        print(order_product.id)
        new_quantity = order_product.quantity +1
        order_product.update(quantity=new_quantity)
