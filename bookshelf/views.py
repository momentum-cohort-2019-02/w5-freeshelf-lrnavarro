from django.shortcuts import render
from bookshelf.models import Book, Author
# from . import csv

# Create your views here.
def index(request):
    return render(request, 'index.html')

#     with open('Lis of Books2') as file:
#         book_list = [line.split() for line in file]
#     return elevation_list

# get_2d_array('elevation_small.txt')
    