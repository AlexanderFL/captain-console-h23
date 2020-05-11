from django.urls import path
from . import views



urlpatterns = [
    path('<int:id>', views.index, name="account_index"),
    path('edit/<int:id>', views.edit, name="account_edit_profile"),
]

