from django import forms
from .models import contacto

#formulario para el modelo contacto 
class ContactForm(forms.ModelForm):

    class Meta:
        models = contacto
        fiels = ['nombre', 'correo', 'telephono', 'description']