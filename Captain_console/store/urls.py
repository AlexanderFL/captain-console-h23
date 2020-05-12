from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="store_index"),
    path('<int:id>', views.get_product_by_id, name="product_details"),
    path('search/<str:query>', views.search, name="search_page")
]