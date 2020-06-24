from django import forms
from django.contrib.auth.models import User
from Login_app import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = models.User
        fields = ('username', 'password', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = models.UserInfo
        fields = ('facebook_id', 'profile_pic')
