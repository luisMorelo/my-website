from django.urls import path
from .import views

urlpatterns = [
    path('', views.my_vista, name= 'my vista principal'),
    path('resume', views.view_resume, name='resumen')
]
