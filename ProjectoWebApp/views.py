from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return render(request,'ProjectoWebApp/template/ProjectoWebApp/home.html')
def tienda(request):
    return render(request,'ProjectoWebApp/template/ProjectoWebApp/tienda.html')

