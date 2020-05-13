from django.urls import path
from . import views

urlpatterns = [
    path('contactinfo/', views.index, name="checkout_index"),
    path('shipping/', views.shipping, name="checkout_shipping"),
    path('payment/', views.payment, name="checkout_payment"),
    path('confirmation/', views.confirmation, name="checkout_confirmation"),
]

