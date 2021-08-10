from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# The fields listed here are the fields that will be listed on the
# user creation form (this modifies the default sign up page provided by Django).
# In this class, it is adding the email field to the form.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']