from django.urls import path
from . import views

urlpatterns = [
    path('', views.crymain, name='converter')
]
