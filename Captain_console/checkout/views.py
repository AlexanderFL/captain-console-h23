from django.shortcuts import render
from account.models import User

# Create your views here.
def index(request, id=None):
    context = {
        'page_checkout': 'contactinfo',
    }
    if id != None:
        context['user'] = User.objects.get(pk=id)
    return render(request, 'checkout/index.html', context)

def shipping(request, id=None):
    context = {
        'page_checkout': 'shipping',
    }
    if id != None:
        context['user'] = User.objects.get(pk=id)
    return render(request, 'checkout/index.html', context)

def payment(request, id=None):
    context = {
        'page_checkout': 'paymentinfo',
    }
    if id != None:
        context['user'] = User.objects.get(pk=id)
    return render(request, 'checkout/index.html', context)

def confirmation(request, id=None):
    context = {
        'page_checkout': 'confirmation',
    }
    if id != None:
        context['user'] = User.objects.get(pk=id)
    return render(request, 'checkout/index.html', context)

