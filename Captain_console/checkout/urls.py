from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="checkout_index"),
    path('contactinfo', views.contactinfo, name="contactinfo_index"),
    path('contactinfo/shipping', views.shipping, name="shipping_index"),
    path('contactinfo/shipping/payment', views.payment, name="payment_index")
]