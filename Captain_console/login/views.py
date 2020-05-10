from django.shortcuts import render, redirect
import bcrypt  # pip install bcrypt

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from account.models import User


def index(request):
    return render(request, 'login/index.html', context={'page_login': 'login_index'})


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(str(request.POST.get("password")).encode('utf-8'), salt)

        if not User.email_already_exists(email):
            User.insert(username, email, password)
            return redirect('login_index')

    return render(request, 'login/index.html', context={'page_login': 'login_register'})