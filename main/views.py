from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.models import *
from django.shortcuts import get_object_or_404

class KorisnikList(ListView):
    model = Korisnik
    context_object_name = 'korisnici'
    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(ime__icontains=query) | Q(prezime__icontains=query)
            )

        vip_filter = self.request.GET.get('vip')
        if vip_filter is not None:
            queryset = queryset.filter(vip=vip_filter.lower() == 'true')

        return queryset

class KorisnikCreate(CreateView):
    model = Korisnik
    fields = ['ime', 'prezime', 'mjesto', 'dob', 'vip']
    template_name = 'main/korisnik_form.html'
    success_url = reverse_lazy('korisnik_list')

class KorisnikUpdate(UpdateView):
    model = Korisnik
    fields = ['ime', 'prezime', 'mjesto', 'dob', 'vip']
    template_name = 'main/korisnik_form.html'
    success_url = reverse_lazy('korisnik_list')

class KorisnikDelete(DeleteView):
    model = Korisnik
    template_name = 'main/korisnik_confirm_delete.html'
    success_url = reverse_lazy('korisnik_list')
    
class OglasList(ListView):
    model = Oglas
    context_object_name = 'oglasi'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(predmet__icontains=query) | Q(mjesto__icontains=query) 
            )

        razmjena_filter = self.request.GET.get('razmjena')
        if razmjena_filter is not None:
            queryset = queryset.filter(razmjena=razmjena_filter.lower() == 'true')

        return queryset

class OglasCreate(CreateView):
    model = Oglas
    fields = ['prodavatelj', 'predmet', 'mjesto', 'cijena', 'razmjena']
    template_name = 'main/oglas_form.html'
    success_url = reverse_lazy('oglas_list')

class OglasUpdate(UpdateView):
    model = Oglas
    fields = ['prodavatelj', 'predmet', 'mjesto', 'cijena', 'razmjena']
    template_name = 'main/oglas_form.html'
    success_url = reverse_lazy('oglas_list')

class OglasDelete(DeleteView):
    model = Oglas
    template_name = 'main/oglas_confirm_delete.html'
    success_url = reverse_lazy('oglas_list')

def index(request):
    return render(request, 'main/index.html')

def home(request):
    return render(request, 'base_generic.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)