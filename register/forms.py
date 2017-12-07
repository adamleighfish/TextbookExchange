from django import forms
from django.contrib.auth.models import User
from register.models import School

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password Confirmation",widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','first_name','last_name', 'password')

    def clean_password2(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class SchoolForm(forms.ModelForm):
    class Meta():
        model = School
        fields = ('school', 'state', 'city')
