from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

# --- AUTHENTICATION & REGISTRATION ---

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Saves the new user to the database
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'books/register.html', {'form': form})


# --- CRUD OPERATIONS (Create, Read, Update, Delete) ---

# READ: List all books. @login_required ensures Sessions are active.
@login_required 
def book_list(request):
    # ORM query: fetch all books from the database
    books = Book.objects.all() 
    return render(request, 'books/book_list.html', {'books': books})

# CREATE: Add a new book
@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.added_by = request.user # Attach logged-in user to the book
            book.save() # Save to database
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# UPDATE: Edit an existing book
@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

# DELETE: Remove a book
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete() # ORM command to delete
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})