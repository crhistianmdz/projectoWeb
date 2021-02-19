from django.shortcuts import render, HttpResponse

# Create your views here.


def home(reques):
    return HttpResponse('Home')
def servicios(reques):
    return HttpResponse('Servicios')
def tienda(reques):
    return HttpResponse('Tienda')
def blog(reques):
    return HttpResponse('Blog')
def contacto(reques):
    return HttpResponse('Contacto')