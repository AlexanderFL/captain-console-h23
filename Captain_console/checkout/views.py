from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def contactinfo(request):
    return render(request, 'checkout/contactinfo.html')