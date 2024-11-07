from django.shortcuts import render, redirect
from .forms import ContactForm
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
            return redirect('my vista principal')
        return render(request, 'contact.html', {'form': form})