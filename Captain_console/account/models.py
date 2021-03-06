from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=512)
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.username

    @staticmethod
    def insert(username, email, password):
        User.objects.create(username=username, email=email, password=password)
        return User.objects.get(email=email)

    """
        Checks if email already exists in the database
        Returns True if email exists, False otherwise
    """

    @staticmethod
    def email_already_exists(email):
        data_count = User.objects.filter(email=email).count()
        if data_count == 0:
            return False
        else:
            return True

    @staticmethod
    def get_password(email):
        user_obj = User.objects.filter(email=email)
        for user in user_obj:
            return user.password
        return None

    @staticmethod
    def get_password_from_id(id):
        user_obj = User.objects.filter(pk=id)
        for user in user_obj:
            return user.password
        return None

    @staticmethod
    def update_user_password(id, new_password):
        User.objects.filter(pk=id).update(password=new_password)


class PaymentInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    exp_date = models.CharField(max_length=6)
    card_number = models.CharField(max_length=19)
    cvc = models.CharField(max_length=3, blank=True)

    @staticmethod
    def insert(user_id, name, number, exp, cvc):
        try:
            PaymentInfo.objects.get(user_id=user_id)
            PaymentInfo.objects.filter(user_id=user_id).update(user_id=user_id, name=name, card_number=number,
                                                            exp_date=exp, cvc=cvc)
        except:
            PaymentInfo.objects.create(user_id=user_id, name=name, card_number=number, exp_date=exp, cvc=cvc)


class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)

    @staticmethod
    def insert(user_id, address, city, country, zip_code):
        try:
            Address.objects.get(user_id=user_id)
            Address.objects.filter(user_id=user_id).update(address=address, city=city, country=country, zip_code=zip_code)
        except:
            Address.objects.create(user_id=user_id, address=address, city=city, country=country, zip_code=zip_code)


class UserPhoto(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.CharField(max_length=200)
    alt = models.CharField(max_length=128, blank=True)

    @staticmethod
    def insert(user_id, path, alt):
        UserPhoto.objects.update_or_create(user_id=user_id, path=path, alt=alt)

    @staticmethod
    def update_photo(user_id, path):
        UserPhoto.objects.filter(user_id=user_id).update(path=path)
