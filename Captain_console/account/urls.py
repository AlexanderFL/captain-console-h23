from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="account_index"),
    path('edit', views.edit, name="account_edit_profile"),
]

