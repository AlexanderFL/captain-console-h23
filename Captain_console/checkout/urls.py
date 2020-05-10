from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="checkout_index"),
    path('<int:id>', views.index, name="checkout_index"),

    path('contactinfo/', views.index, name="checkout_index"),
    path('contactinfo', views.index, name="checkout_index"),
    path('contactinfo/<int:id>', views.index, name="checkout_index"),

    path('shipping/', views.shipping, name="checkout_shipping"),
    path('shipping', views.shipping, name="checkout_shipping"),
    path('shipping/<int:id>', views.shipping, name="checkout_shipping"),

    path('payment/', views.payment, name="checkout_payment"),
    path('payment', views.payment, name="checkout_payment"),
    path('payment/<int:id>', views.payment, name="checkout_payment"),

    path('confirmation/', views.confirmation, name="checkout_confirmation"),
    path('confirmation', views.confirmation, name="checkout_confirmation"),
    path('confirmation/<int:id>', views.confirmation, name="checkout_confirmation"),
]

