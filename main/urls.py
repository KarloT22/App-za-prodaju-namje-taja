from django.urls import path
from . import views
from main.views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='base_generic'),

    path('home/korisnici/', KorisnikList.as_view(), name="korisnik_list"),
    path('home/korisnici/create/', KorisnikCreate.as_view(), name='create_korisnik'),
    path('home/korisnici/<int:pk>/update/', KorisnikUpdate.as_view(), name='update_korisnik'),
    path('home/korisnici/<int:pk>/delete/', KorisnikDelete.as_view(), name='delete_korisnik'),

    path('home/oglasi/', OglasList.as_view(), name="oglas_list"),
    path('home/oglasi/create/', OglasCreate.as_view(), name='create_oglas'),
    path('home/oglasi/<int:pk>/update/', OglasUpdate.as_view(), name='update_oglas'),
    path('home/oglasi/<int:pk>/delete/', OglasDelete.as_view(), name='delete_oglas'),

]