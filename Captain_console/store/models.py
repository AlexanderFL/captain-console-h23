from django.db import models
from account.models import User

class Category(models.Model):
    name = models.CharField(max_length=64)

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    discount = models.FloatField(null=True)
    copies_sold = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    average_rating = models.FloatField(null=True)


    """
    Sets average rating of a product
    """
    def set_rating(self, rating, prod_id):
        Product.objects.filter(pk=prod_id).update(average_rating="{:.2f}".format(rating))

    """
    Returns average rating of a product
    """

    def get_rating(self):
        reviews = Review.objects.filter(product_id=self.id)

        total_ratings = 0
        for review in reviews:
            total_ratings += review.rating
        avg_rating = total_ratings / len(reviews)
        return avg_rating

    def __str__(self):
        return self.name

    """
        Returns the discounted price with two decimal numbers
    """

    def get_discounted_price(self):
        return "{:.2f}".format(self.price * 0.01 * (100 - self.discount))

    """
        Returns the total discount and removes any trailing zeros from float,
        ex. '50.0 => 50', and '13.5 => 13.5'
    """

    def get_discount(self):
        return "{:g}".format(self.discount)


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

    def create_review(self, prod_id, user_id, rating):
        Review.objects.create(product_id=prod_id, user_id=user_id, rating=rating, comment="")

    def __str__(self):
        return str(self.rating)



