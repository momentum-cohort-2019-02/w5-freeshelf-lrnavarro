from django.shortcuts import render
from bookshelf.models import Book, Author
# from . import csv

# Create your views here.
def index(request):
    books = Book.objects.all()

    #respond with index.html inside of templates/bookshelf and send books so they can be used in the index.html
    response = render(request, 'bookshelf/index.html', {
        "books": books,
    })
    return response

    