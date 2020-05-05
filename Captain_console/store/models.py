from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    discount = models.FloatField()
    copies_sold = models.IntegerField()


class Genres(models.Model):
    genre = models.CharField(max_length=32)


class Developers(models.Model):
    developer = models.CharField(max_length=64)


class ProductDetails(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete=models.CASCADE)
    developer_id = models.ForeignKey(Developers, on_delete=models.CASCADE)
    release_date = models.DateField()
    description = models.CharField(max_length=1024)
