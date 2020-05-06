from django.shortcuts import render
from store.models import Product


def index(request):
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'store/index.html', context)