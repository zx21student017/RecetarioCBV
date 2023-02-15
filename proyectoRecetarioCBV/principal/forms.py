from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields=['nombre','subnombre','ingredientes','imagen','receta','author','categorias']
        widgets = {
            'nombre': forms.TextInput(attrs={'style':'background-color:red'}),
            'subnombre': forms.TextInput(attrs={'placeholder':'Escribe el subnombre','style':'background-color:yellow'}),
            'ingredientes': forms.TextInput(attrs={'class':'btn'}),
        }
        labels = {
            'subnombre': '',
        }