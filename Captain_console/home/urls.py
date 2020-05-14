from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_index"),
    path('logout', views.logout, name="home_index_logout")
]
