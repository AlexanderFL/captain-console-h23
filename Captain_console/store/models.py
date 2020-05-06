from django.db import models
from account.models import User


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    discount = models.FloatField(null=True)
    copies_sold = models.IntegerField()
    def __str__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=128)


class Developer(models.Model):
    developer = models.CharField(max_length=128)


class ProductDetails(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    developer_id = models.ForeignKey(Developer, on_delete=models.CASCADE)
    release_date = models.DateField()
    description = models.TextField()


class ProductPhoto(models.Model):
    path = models.CharField(max_length=999)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    alt = models.CharField(max_length=128, blank=True)
    def __str__(self):
        return self.path


class Review(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True)


# Maybe these models can change locations but I'll leave it here for now
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.FloatField()
    tracking_nr = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)


class OrderProduct(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()


#######################



















