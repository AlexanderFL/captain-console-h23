from django.shortcuts import render
from store.models import ProductPhoto


def index(request):
    context = {'products': ProductPhoto.objects.all()[:4]}
    return render(request, 'home/index.html', context)
