from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'login/index.html', context={'page_login': 'login_index'})


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(username)
        print(email)
        print(password)

    return render(request, 'login/index.html', context={'page_login': 'login_register'})