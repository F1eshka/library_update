from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Reader
from .forms import BookForm, ReaderForm

def index(request):
    return render(request, 'catalog/index.html')

def book_list(request):
    view_mode = request.GET.get('filter')

    if view_mode == 'available':
        books = Book.objects.filter(is_available=True)
    else:
        books = Book.objects.all()

    return render(request, 'catalog/book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'catalog/book_detail.html', {'book': book})

def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'catalog/reader_list.html', {'readers': readers})

def reader_detail(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    return render(request, 'catalog/reader_detail.html', {'reader': reader})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm()
    return render(request, 'catalog/book_form.html', {'form': form, 'title': 'Додати книгу'})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = BookForm(instance=book)
    return render(request, 'catalog/book_form.html', {'form': form, 'title': 'Редагувати книгу'})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('/books/')
    return render(request, 'catalog/book_confirm_delete.html', {'object': book})


def reader_create(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/readers/')
    else:
        form = ReaderForm()
    return render(request, 'catalog/reader_form.html', {'form': form, 'title': 'Додати читача'})

def reader_update(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        form = ReaderForm(request.POST, instance=reader)
        if form.is_valid():
            form.save()
            return redirect('/readers/')
    else:
        form = ReaderForm(instance=reader)
    return render(request, 'catalog/reader_form.html', {'form': form, 'title': 'Редагувати читача'})

def reader_delete(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        reader.delete()
        return redirect('/readers/')
    return render(request, 'catalog/reader_confirm_delete.html', {'object': reader})