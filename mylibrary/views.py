from django.shortcuts import render
from . models import Book, BookInstance, Author

# Create your views here.
def home(request):
    return render(request, 'mylibrary/index.html', {'books' : Book.objects.all()})


def book_instance(request, received_id):
    return render(request, 'mylibrary/bookInstance.html', {'bookIns': BookInstance.objects.get(id=received_id)})

def authors(request):
    return render(request, 'mylibrary/author_list.html', {'authors' : Author.objects.all()})
