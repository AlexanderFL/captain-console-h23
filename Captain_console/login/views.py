from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'login/index.html', context={'page_login': 'login_index'})

def register(request):
    return render(request, 'login/index.html', context={'page_login': 'login_register'})