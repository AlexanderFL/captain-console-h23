from django.shortcuts import render
from store.models import Product
from home.models import News


def index(request):
    context = {'products': Product.objects.all()[:3], 'articles': News.objects.all().order_by('-date')[:3]}
    return render(request, 'home/index.html', context)


def terms(request):
    context = {'products': Product.objects.all()[:3]}
    return render(request, 'home/terms.html', context)


def aboutus(request):
    context = {'products': Product.objects.all()[:3]}
    return render(request, 'home/aboutus.html', context)


def logout(request):
    if request.session.__contains__('user_id'):
        request.session.pop('user_id')
    context = {'products': Product.objects.all()[:3]}
    return render(request, 'home/index.html', context)


def readmore(request, id=None):
    if id != None :
        print("readmore id: {}".format(id))

        return render(request, 'home/article.html', {'article': News.objects.get(pk=id)})
    else :
        print("readmore failed")
    # return render(request, '')
