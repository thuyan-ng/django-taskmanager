from django import forms
from .models import Developer
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class DeveloperForm(UserCreationForm):
    # first_name = forms.CharField(label="First name", max_length=100)
    # last_name = forms.CharField(max_length=100)
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name', 'username', 'email',]

class DeveloperChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name', 'username', 'email',]

class ShortDeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        fields = ['first_name', 'last_name', 'username']