from django.shortcuts import render
from .models import *
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()
    num_books_spider = Book.objects.filter(title__contains='spider').count()
    context = {'num_books': num_books, 'num_instances': num_instances, 'num_instances_available':
        num_instances_available, 'num_authors': num_authors, 'num_genre': num_genre, 'num_books_spider':
               num_books_spider}
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author
