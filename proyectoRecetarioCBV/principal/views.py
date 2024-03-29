from django.shortcuts import render
from . models import Receta
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import RecetaForm
from django.contrib.auth.mixins import LoginRequiredMixin#sirve para que el usuario no acceda a funciones sin estar logueado

class RecetaListView(ListView):
    model = Receta

class RecetaDetailView(DetailView):
    model = Receta

# @method_decorator
class RecetaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/cuentas/login/'
    model = Receta
    form_class=RecetaForm
    success_url = reverse_lazy('receta')

class RecetaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/cuentas/login/'
    model = Receta
    form_class = RecetaForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('receta')

class RecetaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/cuentas/login/'
    model = Receta
    success_url = reverse_lazy('inicio')