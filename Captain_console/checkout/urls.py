from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="checkout_index"), #/checkout
    path('contactinfo', views.contactinfo, name="contactinfo_index"),
    path('shipping', views.shipping, name="shipping_index"),
    path('payment', views.payment, name="payment_index"),
    path('confirmation', views.confirmation, name="confirmation_index"),
]

# urlpatterns = [
#     path('', views.index, name="checkout_index"), #/checkout
#     path('contactinfo', views.contactinfo, name="contactinfo_index"),
#     path('contactinfo/shipping', views.shipping, name="shipping_index"),
#     path('contactinfo/shipping/payment', views.payment, name="payment_index"),
#     path('contactinfo/shipping/payment/confirmation', views.confirmation, name="confirmation_index"),
# ]