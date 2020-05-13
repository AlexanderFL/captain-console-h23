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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    '''
    Checks if user has a non-confirmed order ("shopping cart")
    '''

    def check_active_order(self, user_id):
        empty_order = False
        orders = Order.objects.filter(pk=user_id)
        for order in orders:
            if order.confirmed == False:  # Shopping cart
                shopping_cart = order
                print("Emtpy order with id: " + str(shopping_cart.id))
                empty_order = True

            if empty_order == False:  # No items in shopping cart, create non-confirmed order
                new_order = Order.objects.create(user_id=user_id)
                shopping_cart = new_order
                print("Creating new order with id: " + str(shopping_cart.id))
        return shopping_cart

    '''
    Price calculated
    '''

    def calculate_price(self, quantity, product):
        total_price = product.price * quantity * (100 - product.discount) / 100
        print("Total price is:" + str(total_price))
        return total_price

    '''
    Checks if product is already in cart
    '''

    def check_if_already_in_cart(self, user_id, product):
        order_products = OrderProduct.objects.filter(user_id=user_id)
        for order_product in order_products:
            if order_product.product_id.id == product.id:
                return order_product
        return False

    '''
    Creates a new order_product in cart
    '''

    def create_product_in_cart(self, product, quantity, user, shopping_cart):
        total_price = self.calculate_price(quantity, product)
        OrderProduct.objects.create(product_id=product, quantity=quantity, price=total_price, user_id=user,
                                    order_id=shopping_cart)
        print("New item added to cart")

    '''
    Updates product in cart
    '''

    def update_product_in_cart(self, order_product, quantity, user, shopping_cart):
        new_quantity = order_product.quantity + quantity
        total_price = self.calculate_price(new_quantity, order_product.product_id)
        print(order_product)
        OrderProduct.objects.filter(pk=order_product.id).update(quantity=new_quantity, price=total_price)
        print("Item updated in cart")

    '''
    Adds product to cart or updates quantity if already in cart
    '''

    def add_product_to_cart(self, product_id, quantity, user_id):
        user = User.objects.get(pk=user_id)
        product = Product.objects.get(pk=product_id)

        # Get order id for active non-confirmed order
        shopping_cart = self.check_active_order(user_id)

        # Check if item is in cart
        in_cart = self.check_if_already_in_cart(user_id, product)

        if not in_cart:
            self.create_product_in_cart(product, quantity, user, shopping_cart)
        else:
            self.update_product_in_cart(in_cart, quantity, user, shopping_cart)

    # # Increase quantity of item in cart
    # def add_item(self, prod_id):
    #     print(prod_id)
    #     order_product = Product.objects.get(pk=prod_id)
    #     print(order_product.id)
    #     new_quantity = order_product.quantity + 1
    #     order_product.update(quantity=new_quantity)
