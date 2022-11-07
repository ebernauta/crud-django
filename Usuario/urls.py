from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('agregarUsuarios/', views.agregarUsuarios, name='agregarUsuarios'),
    path('listarUsuarios/', views.listarUsuarios, name='listarUsuarios'),
    path('eliminarUsuarios/<str:rut>', views.eliminarUsuarios, name='eliminarUsuarios'),
    path('editarUsuarios/<str:rut>', views.editarUsuarios, name='editarUsuarios'),
]
