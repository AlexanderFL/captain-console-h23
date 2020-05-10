from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=512)
    email = models.CharField(max_length=128)
    def __str__(self):
        return self.username


class PaymentInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    exp_date = models.DateField()
    card_number = models.CharField(max_length=19)
    cvc = models.CharField(max_length=3, blank=True)


class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)


class UserPhoto(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)
    alt = models.CharField(max_length=128, blank=True)



