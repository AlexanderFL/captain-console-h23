from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="login_index"),
    path('register', views.register, name="login_register"),
]