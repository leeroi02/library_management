from django import forms
from .models import Book

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('borrowed_by', 'due_date')