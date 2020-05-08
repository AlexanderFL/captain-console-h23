from django.urls import path
from . import views



urlpatterns = [
    path('<int:id>', views.index, name="account_index"),
    path('change_profile/<int:id>', views.edit, name="change_profile")
]

