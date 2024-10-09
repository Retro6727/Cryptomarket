from django.urls import path
from . import views

urlpatterns = [
    path('', views.show, name="home"),
    path('register/', views.register, name="register"),
    path('thank/', views.thankyou, name="thanks"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('about/', views.about, name='abouts'),
    path('blog/', views.blog, name='blogs'),
    path('stocks/', views.stocks, name='stock_exchange'),
    
]