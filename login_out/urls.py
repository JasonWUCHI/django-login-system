from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('login/' , views.loginView , name = 'login'),
    path('inner/' , views.innerPageView , name = 'inner'),
    path('logout/' , views.logoutView , name = 'logout'),
    path('register/' , views.registerView , name = 'register')
]