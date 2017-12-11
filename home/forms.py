from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import Book, School


class HomeForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ("ISBN",)


class UserForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('school', 'state', 'city')
