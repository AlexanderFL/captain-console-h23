import json

import bcrypt  # pip install bcrypt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from account.models import User, UserPhoto
from account.views import index as account_index


@csrf_exempt
def index(request):
    print("login/view/index: I'm executed")
    if request.method == "POST":
        print("login/view/index: Post method")
        email = request.POST.get("email").lower()
        # Encode the plain password into bytes
        plain_password = request.POST.get("password").encode('utf-8')
        # Get the stored password in the database
        stored_password = User.get_password(email)

        if stored_password is not None:
            # Encode the password stored in the database to bytes
            hashed_pass = stored_password.encode('utf-8')

            # Compare the plain password to the stored hash
            if bcrypt.checkpw(plain_password, hashed_pass):
                request.session['user_id'] = User.objects.get(email=email).id
                url = '/account/'
                print("login/view/index: User " + str(request.session['user_id']) + " was authenticated")
                response = json.dumps({'status': 200, 'message': url})
                return HttpResponse(response, content_type='application/json')

        response = json.dumps({'status': 0, 'message': 'Email/password was incorrect'})
        return HttpResponse(response, content_type='application/json')
    return render(request, 'login/index.html', context={'page_login': 'login_index'})


@csrf_exempt
def register(request):
    if request.method == "POST":

        # Get the user data from POST
        username = request.POST.get("username")
        email = str(request.POST.get("email")).lower()
        # Encode the plain password into bytes
        password = str(request.POST.get("password")).encode('utf-8')

        # Hash the password with salt
        password_hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        # Check if email has already been registered
        if not User.email_already_exists(email):
            # Get password back into str before storing it in database
            password_hashed = password_hashed.decode('utf-8')
            user_inserted = User.insert(username, email, password_hashed)
            # Insert a default picture that the user sees
            link = "https://photos.alexfreyr.com/profile/default-profile.png"
            alt = "Default profile picture for user"
            UserPhoto.insert(user_inserted, link, alt)

            # Create the session for the user and redirect him to his account page
            request.session['user_id'] = user_inserted.id
            response = json.dumps({'status': 200, 'message': '/account/'})
            return HttpResponse(response, content_type='application/json')
        else:
            response = json.dumps({'status': 0, 'message': 'This email is already in use'})
            return HttpResponse(response, content_type='application/json')
    return render(request, 'login/index.html', context={'page_login': 'login_register'})
