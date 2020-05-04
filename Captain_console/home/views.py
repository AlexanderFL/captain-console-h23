from django.shortcuts import render

# Create your views here.

context = [
    {'name': 'supermario','price': 123},
    {'name': 'crashbandicoot',"price": 50}]

def index(request):
    return render(request, 'home/index.html', context={"data": context})