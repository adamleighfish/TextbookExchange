from django import forms
from home.models import Book

class homeForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("ISBN",)
