from django.shortcuts import render

# Create your views here.
def crymain(request):
    return render(request, 'index.html')