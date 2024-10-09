from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email_address = forms.EmailField()
    mobile = forms.IntegerField()
    username = forms.CharField(max_length=100)
    class Meta:
        model = User          
        fields = ['first_name', 'last_name', 'email_address', 'mobile', 'username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())


class CyptoconvertForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    from_currency = forms.ChoiceField(label='From Currency', choices=[
            ('BTC', 'Bitcoin(BTC)'),
            ('ETH', 'Ethereum(ETH)'),
            ('USDT', 'Tether(USDT)'),
            ('DOGE', 'DogeCoin(DOGE)'),
            ('BNB', 'BNB(BNB)')
        ])
    
    to_currency = forms.ChoiceField(label='To Currency', choices=[
        ('BTC', 'Bitcoin(BTC)'),
        ('ETH', 'Ethereum(ETH)'),
        ('USDT', 'Tether(USDT)'),
        ('DOGE', 'DogeCoin(DOGE)'),
        ('BNB', 'BNB(BNB)')
    ])
    converted_amount = forms.DecimalField(label='Converted Amount', max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

