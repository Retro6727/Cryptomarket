from django import forms
from . import models

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = models.Userlogin
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }