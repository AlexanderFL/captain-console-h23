from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="checkout_index"),
    path('/contactinfo', views.contactinfo, name="contactinfo_index")
]