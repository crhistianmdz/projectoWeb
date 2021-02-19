from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request,'ProjectoWebApp/home.html')
def servicios(request):
    return render(request,'ProjectoWebApp/servicios.html')
def tienda(request):
    return render(request,'ProjectoWebApp/tienda.html')
def blog(request):
    return render(request,'ProjectoWebApp/blog.html')
def contacto(request):
    return render(request,'ProjectoWebApp/contacto.html')