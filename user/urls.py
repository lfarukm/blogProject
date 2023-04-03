from django.urls import path    
from .views import *


urlpatterns = [
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name='login'),
    path('logout/', userlogout, name='logout'),
    path('profile/<str:slug>',profil, name='profil'),
    path('update/',update, name='update'),
    path('change/', reset, name='reset')
]