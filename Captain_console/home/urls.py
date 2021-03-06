from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home_index"),
    path('terms', views.terms, name="home_terms"),
    path('aboutus', views.aboutus, name="home_aboutus"),
    path('logout', views.logout, name="home_index_logout"),
    path('readmore', views.readmore, name="read_more"),
    path('readmore/<int:id>', views.readmore, name="read_more"),
]
