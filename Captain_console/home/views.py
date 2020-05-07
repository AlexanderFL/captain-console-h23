from django.shortcuts import render
from store.models import ProductPhoto


def index(request):
    context = {'products': ProductPhoto.objects.all()[:4], 'user_session': request.session.get('user_session')}
    return render(request, 'home/index.html', context)
