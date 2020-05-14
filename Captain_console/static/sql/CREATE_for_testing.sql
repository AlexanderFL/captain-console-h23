

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=512)
    email = models.CharField(max_length=128)


class PaymentInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    exp_date = models.CharField(max_length=6)
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


class Category(models.Model):
    name = models.CharField(max_length=64)

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    discount = models.FloatField(null=True)
    copies_sold = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    average_rating = models.FloatField(null=True)



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

class OrderProduct(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()


class Order(models.Model):
    total_price = models.FloatField()
    tracking_nr = models.CharField(max_length=128)
    OrderCart_id = models.ForeignKey(OrderCart, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)


class OrderCart(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    orderproduct_id = models.ForeignKey(OrderProduct, on_delete=models.CASCADE)

