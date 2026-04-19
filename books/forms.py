from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
        # Note: We exclude 'added_by' because we will set that automatically based on the logged-in user.