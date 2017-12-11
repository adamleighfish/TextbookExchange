from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import Book, School , Listing


class HomeForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ("ISBN",)


class UserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'first_name','email', 'last_name', 'password1', 'password2',)


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('school', 'state', 'city')


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'

