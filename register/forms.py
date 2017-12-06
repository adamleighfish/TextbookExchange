from django import forms
from django.contrib.auth.models import User
from register.models import School

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'email', 'password')

class SchoolForm(forms.ModelForm):
    class Meta():
        model = School
        fields = ('school', 'state', 'city')
