from django.shortcuts import render

# Create your views here.

def my_vista(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    


def view_resume(request):
    if request.method == 'GET':
        return render(request, 'resume.html')