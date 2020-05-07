from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'checkout/index.html')

def contactinfo(request):
    return render(request, 'checkout/contactinfo.html')

def shipping(request):
    return render(request, 'checkout/shipping.html')

def payment(request):
    return render(request, 'checkout/payment.html/')

def confirmation(request):
    return render(request, 'checkout/confirmation.html')