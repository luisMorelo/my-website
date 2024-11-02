from django.urls import path
from .import views

urlpatterns = [
    path('', views.my_vista, name= 'my vista principal'),
    path('resume', views.view_resume, name='resumen'),
    path('projects', views.view_project, name='projects'),
    path('contact', views.view_contacto, name='contacto' )
]
