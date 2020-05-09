from django.shortcuts import render
from store.models import Product


def index(request):
    context = {'products': Product.objects.all()[:3], 'user_session': request.session.get('user_session')}
    return render(request, 'home/index.html', context)
