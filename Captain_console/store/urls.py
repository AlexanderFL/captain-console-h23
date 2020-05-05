from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="store_index"),
    path('games', views.index, name="games_index"),
    path('consoles', views.index, name="consoles_index")
]