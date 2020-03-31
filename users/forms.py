from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class MyChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
       super(MyChangeForm, self).__init__(*args, **kwargs)
       del self.fields['password']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MediaForm(forms.ModelForm):
    
    class Meta:
        model = Media
        fields = ['image_name', 'image_description', 'image_image']

class SettingsForm(MyChangeForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email')



    

