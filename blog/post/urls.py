from django.urls import path
from .views import  agregar_post

urlpatterns = [
    path('agregar_post/', agregar_post, name='agregar_post'),
]
