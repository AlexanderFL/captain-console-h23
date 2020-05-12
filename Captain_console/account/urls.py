from django.urls import path
from . import views
from login.views import index as login_views



urlpatterns = [
    path('<int:id>', views.index, name="account_index"),
    path('', login_views, name="account_index"),

    path('edit/<int:id>', views.edit, name="account_edit_profile"),
    path('edit/', login_views, name="account_edit_profile"),
    path('edit', login_views, name="account_edit_profile"),
]

