from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
# Create your views here.

def my_vista(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    

def view_resume(request):
    if request.method == 'GET':
        return render(request, 'resume.html')
    

def view_project(request):
    if request.method == 'GET':
        return render(request, 'projects.html')
    
    
def view_contacto(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.save()

            # Obtener los datos del formulario
            nombre = request.POST['nombre']
            correo = request.POST['correo']
            telephono = request.POST['telephono']
            description = request.POST['description']

            subject = "Nuevo mensaje de contacto desde el formulario"

            # Crear el contenido del email
            template = render_to_string('correodata.html', {
                'nombre': nombre, 
                'correo': correo, 
                'telephono': telephono, 
                'description': description
            })

            # Crear el correo
            email = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,  # Usar el correo del settings.py
                ['luisalmopi@gmail.com']  # Destinatario
            )

            email.fail_silently = False
            email.send()

            messages.success(request, '¡Enviado con éxito! Muchas gracias, pronto estaremos en contacto.')

            return redirect('contacto')

        return render(request, 'contact.html', {'form': form})