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
    def add_product_to_cart(self, product_id, quantity, user_id):

        #Check if there is a non-confirmed order for this user
        orders = Order.objects.filter(pk=user_id)
        for order in orders:
            status = order.confirmed
            if status == False:     #Shopping cart
                shopping_cart = order.id
                shopping_cart_id = shopping_cart.id
            else:   #No items in shopping cart, create non-confirmed order
                shopping_cart_id = Order.objects.create(user_id=user_id).id

        #Calculate total cost for order_product
        product = Product.objects.get(pk=product_id)
        total_price = product.price * quantity * (100 - product.discount) / 100

        #Create order product
        self.objects.create(product_id=product, quantity=quantity, price=total_price, user_id=user_id, order_id = shopping_cart_id)

    # Increase quantity of item in cart
    def add_item(self, prod_id):
        print(prod_id)
        order_product = Product.objects.get(pk=prod_id)
        print(order_product.id)
        new_quantity = order_product.quantity +1
        order_product.update(quantity=new_quantity)


