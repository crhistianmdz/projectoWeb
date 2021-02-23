from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request,'ProjectoWebApp/template/ProjectoWebApp/home.html')
def tienda(request):
    return render(request,'ProjectoWebApp/template/ProjectoWebApp/tienda.html')
def blog(request):
    return render(request,'ProjectoWebApp/template/ProjectoWebApp/blog.html')
def contacto(request):
    return render(request,'ProjectoWebApp/template/ProjectoWebApp/contacto.html')