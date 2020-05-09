from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'checkout/index.html', context={'page_checkout': 'contactinfo'})

def contactinfo(request):
    return render(request, 'checkout/index.html', context={'page_checkout': 'contactinfo'})

def shipping(request):
    return render(request, 'checkout/index.html', context={'page_checkout': 'shipping'})

def payment(request):
    return render(request, 'checkout/index.html', context={'page_checkout': 'paymentinfo'})

def confirmation(request):
    return render(request, 'checkout/index.html', context={'page_checkout': 'confirmation'})

#
# # Create your views here.
# def index(request):
#     return render(request, 'checkout/index.html', context={'page-checkout'=})
#
# def contactinfo(request):
#     return render(request, 'checkout/contactinfo.html')
#
# def shipping(request):
#     return render(request, 'checkout/shipping.html')
#
# def payment(request):
#     return render(request, 'checkout/paymentinfo.html/')
#
# def confirmation(request):
#     return render(request, 'checkout/confirmation.html')