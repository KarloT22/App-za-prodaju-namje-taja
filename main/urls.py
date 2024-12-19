from django.urls import path
from . import views
from main.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='base_generic'),
    path('home/korisnici/', KorisnikList.as_view()),
    path('home/oglasi/', OglasList.as_view()),
]