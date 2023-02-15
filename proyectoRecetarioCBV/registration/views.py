from django import forms
# from django.contrib.auth.forms import UserCreationForm la cambiamos por la clase
from . forms import UsuarioCrearFormConEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class RegistroView(CreateView):
    form_class = UsuarioCrearFormConEmail
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') + '?registrado'

    def get_form(self, form_class = None):
        form = super(RegistroView, self).get_form()

        form.fields['username'].widget = forms.TextInput(attrs={'style':'background-color:lightgray','placeholder':'Nombre'})
        form.fields['email'].widget = forms.TextInput(attrs={'style':'background-color:lightgrenn','placeholder':'Email'})
        form.fields['password1'].widget = forms.TextInput(attrs={'style':'background-color:lightgray','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.TextInput(attrs={'style':'background-color:lightgray','placeholder':'Contraseña'})

        return form