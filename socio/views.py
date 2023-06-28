from django.shortcuts import render, redirect
from .models import Misperris
from django.contrib import messages

# Create your views here.

def home(request):
    misperrisListado = Misperris.objects.all()
    messages.success(request, '¡Mis perris Listados!')
    return render(request, "gestionmisperris.html", {"misperris": misperrisListado})

def registrarMisperris(request):
    nombre=request.POST['Nombre']
    raza_predominante=request.POST['Raza_Predominante']
    descripcion=request.POST['Descripcion']
    estado=request.POST['Estado']

    Misperris = Misperris.objects.create(nombre=nombre, raza_predominante=raza_predominante, descripcion=descripcion)
    messages.success(request, '¡Mascota registrada!')
    return redirect('/')

def edicionMisperris(request, nombre):
    misperris = Misperris.objects.get(nombre=nombre)
    return render(request, "edicionMisperris.html", {"misperris": misperris})

def editarMisperris(request):
    nombre=request.POST['Nombre']
    raza_predominante=request.POST['Raza_Predominante']
    descripcion=request.POST['Descripcion']
    estado=request.POST['Estado']

    Misperris.nombre = nombre
    Misperris.Raza_Predominante = raza_predominante
    Misperris.descripcion = descripcion
    Misperris.estado = estado
    Misperris.save()

    messages.success(request, '¡Mascota actualizada!')

    return redirect('/')


def eliminarMisperris(request, nombre):
    Misperris = Misperris.objects.get(nombre=nombre)
    Misperris.delete()

    return redirect('/')