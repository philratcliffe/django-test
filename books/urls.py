from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('list/', views.BookList.as_view(), name='book_list'),
]
