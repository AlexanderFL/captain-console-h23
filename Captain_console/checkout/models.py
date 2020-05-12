from django.db import models
from account.models import User
from store.models import Product

class OrderProduct(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    tracking_nr = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)
    orderproduct_id = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)



#######################