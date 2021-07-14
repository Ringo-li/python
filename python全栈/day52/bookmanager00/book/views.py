from os import name
from django.shortcuts import render
from django.http import HttpResponse
from book.models import BookInfo

# Create your views here.
def index(request):
    books = BookInfo.objects.all()
    name = 'Rose'
    context = {
        'books': books,
        'name': name
    }

    return render(request, 'index.html', context)
    return HttpResponse('index')