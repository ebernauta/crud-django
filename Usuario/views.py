from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .form import UsuarioForm
from django.contrib import messages
# Create your views here.

def main(request):
    
    return render(request, 'main.html')

def agregarUsuarios(request):
    
    formulario = UsuarioForm(request.POST or None) #creo el formulario
    if formulario.is_valid():
        formulario.save()
        return redirect('listarUsuarios')
    return render(request, 'agregarUsuarios.html', {'formulario':formulario}) #renderizo el formulario en el template agregarUsuarios.html

def eliminarUsuarios(request, rut):
    Usuarios = Usuario.objects.get(rut=rut)
    Usuarios.delete()
    return redirect('listarUsuarios')

def editarUsuarios(request, rut):
    Usuarios = Usuario.objects.get(rut=rut)
    formulario = UsuarioForm(request.POST or None, instance=Usuarios)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('listarUsuarios')
    return render(request, 'editarUsuarios.html', {'formulario':formulario})

def listarUsuarios(request):
    
    Usuarios = Usuario.objects.all() #obtengo todos los usuarios
    return render(request, 'listarUsuarios.html', {'Usuarios':Usuarios}) #agrego los usuarios a la vista para llamarlo en el html