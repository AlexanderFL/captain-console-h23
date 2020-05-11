from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_index"),
    path('<int:id>', views.index_logout, name="home_index_logout")
]
