import requests
from django.shortcuts import redirect, render, HttpResponse
from .forms import RegisterForm, CyptoconvertForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
#from .serializers import MessageSerializer

# Create your views here.
def show(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("thanks")
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'loginform':form})

def logout(request):
    auth.logout(request)
    return redirect("home")


def thankyou(request):
    return render(request,'ty.html')


#def convert(request):
#    if request.method == "POST":

def about(request):
    return render(request, 'abouts.html')

def blog(request):
    return render(request, 'blogs.html')


def stocks(request):
    cfrm = CyptoconvertForm()
    if request.method == "POST":
        cfrm = CyptoconvertForm(request.POST)
        if cfrm.is_valid():
            amount = cfrm.cleaned_data['amount']
            from_currency = cfrm.cleaned_data['from_currency']
            to_currency = cfrm.cleaned_data['to_currency']
            api_key = 'a6764e16-c6b1-446c-8038-74d6b70ca351'
            url = f'localhost/stock?api_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}'
            response = requests.get(url)
            data = response.json()

            if data.get('success'):
                converted_amount = data['result']
                cfrm.fields['converted_amount'].initial = converted_amount
            else:
                # Handle API errors or invalid data
                error_message = data.get('error_message', 'An error occurred during conversion.')
                return render(request, 'cryptoconvert.html', {'form': cfrm, 'error_message': error_message})

    return render(request, 'stocks.html', {'form': cfrm})