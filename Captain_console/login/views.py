from django.shortcuts import render, redirect
import bcrypt  # pip install bcrypt

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from account.models import User


@csrf_exempt
def index(request):
    if request.method == "POST":
        email = request.POST.get("email").lower()
        # Encode the plain password into bytes
        plain_password = request.POST.get("password").encode('utf-8')
        # Get the stored password in the database
        hashed_pass = User.get_password(email).encode('utf-8')

        # Compare the plain password to the stored hash
        if bcrypt.checkpw(plain_password, hashed_pass):
            print("Match")
        else:
            print("Not match")
    return render(request, 'login/index.html', context={'page_login': 'login_index'})


@csrf_exempt
def register(request):
    if request.method == "POST":

        # Get the user data from POST
        username = request.POST.get("username")
        email = str(request.POST.get("email")).lower()
        password = str(request.POST.get("password")).encode('utf-8')

        # Hash the password with salt
        password_hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        # Check if email has already been registered
        if not User.email_already_exists(email):
            # Get password back into str before storing it in database
            password_hashed = password_hashed.decode('utf-8')
            User.insert(username, email, password_hashed)
            return redirect('login_index')

    return render(request, 'login/index.html', context={'page_login': 'login_register'})
