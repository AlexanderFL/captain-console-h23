from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="checkout_index"), #/checkout
    path('contactinfo', views.contactinfo, name="checkout_contactinfo"),
    path('shipping', views.shipping, name="checkout_shipping"),
    path('payment', views.payment, name="checkout_payment"),
    path('confirmation', views.confirmation, name="checkout_confirmation"),
]

# urlpatterns = [
#     path('', views.index, name="checkout_index"), #/checkout
#     path('contactinfo', views.contactinfo, name="contactinfo_index"),
#     path('contactinfo/shipping', views.shipping, name="shipping_index"),
#     path('contactinfo/shipping/payment', views.payment, name="payment_index"),
#     path('contactinfo/shipping/payment/confirmation', views.confirmation, name="confirmation_index"),
# ]