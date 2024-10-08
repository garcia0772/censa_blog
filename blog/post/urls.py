from django.urls import path
from .views import agregar_post, listar_post, detalle_post, editar_post

urlpatterns = [
    path('agregar_post/', agregar_post, name='agregar_post'),
    path('listar_post/', listar_post, name='listar_post'),
    path('detalle_post/<int:pk>/', detalle_post, name='detalle_post'),
    path('editar_post/<int:pk>/', editar_post, name='editar_post'),
]
