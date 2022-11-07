from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('email: ing.diaz.alvarado@gmail.com <br> teléfono: 5579332570')