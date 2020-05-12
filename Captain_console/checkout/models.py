from django.db import models
from account.models import User
from store.models import Product


class OrderProduct(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

    # Creates new order product in DB
    def add_product_to_cart(self, product_id, quantity, user_id=None):
        product = Product.objects.get(pk=product_id)
        user = User.objects.get(pk=user_id)
        total_price = product.price * quantity * (100 - product.discount) / 100
        OrderProduct.objects.create(product_id=product, quantity=quantity, price=total_price, user_id=user)


class Order(models.Model):
    total_price = models.FloatField()
    tracking_nr = models.CharField(max_length=128)
    orderproduct_id = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
