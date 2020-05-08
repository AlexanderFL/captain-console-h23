from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="store_index"),
    path('games', views.games, name="games_index"),
    path('consoles', views.consoles, name="consoles_index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('search/<str:query>', views.search, name="search_page")
]