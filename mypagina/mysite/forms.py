from django import forms
from .models import Contacto

#formulario para el modelo contacto 
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'telephono', 'description']