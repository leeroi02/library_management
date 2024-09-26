from django.shortcuts import render, redirect
from .models import Book
from .forms import BorrowForm

def book_list(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BorrowForm()
    return render(request, 'books/books_list.html', {'books': books, 'form': form})
