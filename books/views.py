from django.views.generic.list import ListView
from .models import Book

class BookList(ListView):

    model = Book
