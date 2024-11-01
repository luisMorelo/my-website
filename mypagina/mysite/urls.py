from django.urls import path
from .import views

urlpatterns = [
    path('', views.my_vista, name= 'my vista principal')
]
